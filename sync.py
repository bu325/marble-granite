import requests
import datetime
from peewee import *

# Assuming a base URL for your FastAPI/Supabase backend
SYNC_API_BASE_URL = "http://your-backend-api.com/api/v1"

# This is a simplified example. In a real app, you'd handle authentication,
# error handling, and more robust conflict resolution.

def get_last_sync_time():
    # In a real app, this would be stored persistently (e.g., in settings DB)
    return datetime.datetime.min # For now, sync everything from the beginning

def set_last_sync_time(sync_time):
    # In a real app, save this persistently
    pass

def push_data(model_class, records):
    """Pushes local records to the remote server."""
    endpoint = f"{SYNC_API_BASE_URL}/{model_class.__name__.lower()}s"
    headers = {"Content-Type": "application/json"}
    pushed_count = 0
    for record in records:
        data = record.to_dict() # Assuming a to_dict method on BaseModel
        try:
            # Check if record exists remotely by remote_id or try to create
            if hasattr(record, 'remote_id') and record.remote_id:
                response = requests.put(f"{endpoint}/{record.remote_id}", json=data, headers=headers)
            else:
                response = requests.post(endpoint, json=data, headers=headers)

            response.raise_for_status()
            remote_data = response.json()
            # Update local record with remote_id and latest version
            if hasattr(record, 'remote_id'):
                record.remote_id = remote_data.get('id')
            record.version = remote_data.get('version', record.version) # LWW: server version wins
            record.save() # Save updated version and remote_id locally
            pushed_count += 1
        except requests.exceptions.RequestException as e:
            print(f"Error pushing {model_class.__name__} record {record.id}: {e}")
    return pushed_count

def pull_data(model_class, last_sync_time):
    """Pulls remote records from the server."""
    endpoint = f"{SYNC_API_BASE_URL}/{model_class.__name__.lower()}s"
    params = {"updated_since": last_sync_time.isoformat()}
    pulled_count = 0
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        remote_records = response.json()

        for remote_data in remote_records:
            remote_id = remote_data.get('id')
            remote_version = remote_data.get('version', 1)
            remote_updated_at = datetime.datetime.fromisoformat(remote_data.get('updated_at'))

            local_record = None
            if hasattr(model_class, 'remote_id'):
                local_record = model_class.get_or_none(model_class.remote_id == remote_id)

            if local_record:
                # Conflict resolution: Last-Write-Wins (LWW)
                if remote_updated_at > local_record.updated_at:
                    # Remote is newer, update local
                    for key, value in remote_data.items():
                        if hasattr(local_record, key):
                            setattr(local_record, key, value)
                    local_record.save() # This will update updated_at and version
                    pulled_count += 1
                # else: local is newer or same, do nothing (local wins or no change needed)
            else:
                # New record from remote, create locally
                new_record = model_class.create(**remote_data) # This might need careful handling of FKs
                pulled_count += 1

    except requests.exceptions.RequestException as e:
        print(f"Error pulling {model_class.__name__} records: {e}")
    return pulled_count

def sync_all_models():
    """Synchronizes all relevant models."""
    from models.inventory import Material, StockMove
    from models.clients import Client
    from models.workers import Worker, Attendance
    from models.expenses import Expense
    from models.invoices import Invoice, InvoiceItem

    models_to_sync = [
        Material, Client, Worker, Attendance, Expense, Invoice, InvoiceItem, StockMove
    ]

    last_sync = get_last_sync_time()
    current_sync_time = datetime.datetime.now()

    print("Starting synchronization...")
    for model in models_to_sync:
        # Push local changes
        local_changes = model.select().where(model.updated_at > last_sync)
        print(f"Pushing {len(local_changes)} changes for {model.__name__}...")
        push_data(model, local_changes)

        # Pull remote changes
        print(f"Pulling changes for {model.__name__}...")
        pull_data(model, last_sync)

    set_last_sync_time(current_sync_time)
    print("Synchronization complete.")


