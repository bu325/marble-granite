from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.scrollview import MDScrollView

class ClientsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "clients"
        self.build_ui()

    def build_ui(self):
        main_layout = MDBoxLayout(orientation="vertical", padding=20, spacing=10)
        
        # Title
        title = MDLabel(text="إدارة العملاء", theme_text_color="Primary", 
                       size_hint_y=None, height="48dp", halign="center")
        main_layout.add_widget(title)
        
        # Add Client Button
        add_button = MDRaisedButton(text="إضافة عميل جديد", size_hint_y=None, height="48dp")
        add_button.bind(on_release=self.add_client)
        main_layout.add_widget(add_button)
        
        # Clients List
        scroll = MDScrollView()
        self.clients_list = MDList()
        scroll.add_widget(self.clients_list)
        main_layout.add_widget(scroll)
        
        self.add_widget(main_layout)
        self.load_clients()

    def add_client(self, instance):
        print("Add client clicked")

    def load_clients(self):
        # Load clients from database
        for i in range(3):
            item = OneLineListItem(text=f"عميل {i+1}")
            self.clients_list.add_widget(item)

