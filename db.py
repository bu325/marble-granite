from peewee import SqliteDatabase
from models.base import db, BaseModel
from models.inventory import Material, StockMove
from models.clients import Client
from models.workers import Worker, Attendance
from models.expenses import Expense
from models.invoices import Invoice, InvoiceItem

DATABASE = 'marble_granite.db'

def initialize_db():
    db.init(DATABASE)
    db.connect()
    db.create_tables([
        Material, StockMove, Client, Worker, Attendance, Expense, Invoice, InvoiceItem
    ])
    db.close()

# Simple migration example (if needed in the future)
def migrate_db():
    # Add migration logic here if schema changes
    pass


