from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.scrollview import MDScrollView

class InvoicesScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "invoices"
        self.build_ui()

    def build_ui(self):
        main_layout = MDBoxLayout(orientation="vertical", padding=20, spacing=10)
        
        # Title
        title = MDLabel(text="إدارة الفواتير", theme_text_color="Primary", 
                       size_hint_y=None, height="48dp", halign="center")
        main_layout.add_widget(title)
        
        # Create Invoice Button
        create_button = MDRaisedButton(text="إنشاء فاتورة جديدة", size_hint_y=None, height="48dp")
        create_button.bind(on_release=self.create_invoice)
        main_layout.add_widget(create_button)
        
        # Invoices List
        scroll = MDScrollView()
        self.invoices_list = MDList()
        scroll.add_widget(self.invoices_list)
        main_layout.add_widget(scroll)
        
        self.add_widget(main_layout)
        self.load_invoices()

    def create_invoice(self, instance):
        print("Create invoice clicked")

    def load_invoices(self):
        # Load invoices from database
        for i in range(5):
            item = OneLineListItem(text=f"فاتورة {i+1}")
            self.invoices_list.add_widget(item)

