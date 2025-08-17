import os

def get_app_data_dir():
    # In a real Kivy app, this would use App.user_data_dir
    # For now, we'll use a local directory for development
    return "./app_data"

def get_invoice_pdf_path(invoice_number):
    data_dir = get_app_data_dir()
    os.makedirs(data_dir, exist_ok=True)
    return os.path.join(data_dir, f"INV-{invoice_number}.pdf")


