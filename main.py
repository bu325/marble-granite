from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import MDScreenManager

from core.theme import PRIMARY_COLOR, ACCENT_COLOR
from services.db import initialize_db

# Import all screens
from screens.inventory import InventoryScreen
from screens.clients import ClientsScreen
from screens.workers import WorkersScreen
from screens.expenses import ExpensesScreen
from screens.invoices import InvoicesScreen
from screens.reports import ReportsScreen
from screens.settings import SettingsScreen

Builder.load_file("app.kv")

class MainLayout(MDBoxLayout):
    pass

class MarbleGraniteApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "LightBlue"
        return MainLayout()

    def on_start(self):
        initialize_db()

if __name__ == "__main__":
    MarbleGranniteApp().run()

