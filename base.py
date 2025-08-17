from peewee import *
import datetime

db = SqliteDatabase(None) # Will be initialized in services/db.py

class BaseModel(Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    version = IntegerField(default=1) # For optimistic concurrency control in sync
    is_deleted = BooleanField(default=False) # For soft delete

    class Meta:
        database = db

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        self.version += 1
        return super(BaseModel, self).save(*args, **kwargs)


