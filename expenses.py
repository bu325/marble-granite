from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.scrollview import MDScrollView

class ExpensesScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "expenses"
        self.build_ui()

    def build_ui(self):
        main_layout = MDBoxLayout(orientation="vertical", padding=20, spacing=10)
        
        # Title
        title = MDLabel(text="المصاريف الإضافية", theme_text_color="Primary", 
                       size_hint_y=None, height="48dp", halign="center")
        main_layout.add_widget(title)
        
        # Add Expense Button
        add_button = MDRaisedButton(text="إضافة مصروف جديد", size_hint_y=None, height="48dp")
        add_button.bind(on_release=self.add_expense)
        main_layout.add_widget(add_button)
        
        # Expenses List
        scroll = MDScrollView()
        self.expenses_list = MDList()
        scroll.add_widget(self.expenses_list)
        main_layout.add_widget(scroll)
        
        self.add_widget(main_layout)
        self.load_expenses()

    def add_expense(self, instance):
        print("Add expense clicked")

    def load_expenses(self):
        # Load expenses from database
        for i in range(3):
            item = OneLineListItem(text=f"مصروف {i+1}")
            self.expenses_list.add_widget(item)

