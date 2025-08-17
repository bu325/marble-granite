from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.scrollview import MDScrollView

class WorkersScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "workers"
        self.build_ui()

    def build_ui(self):
        main_layout = MDBoxLayout(orientation="vertical", padding=20, spacing=10)
        
        # Title
        title = MDLabel(text="إدارة العمال", theme_text_color="Primary", 
                       size_hint_y=None, height="48dp", halign="center")
        main_layout.add_widget(title)
        
        # Add Worker Button
        add_button = MDRaisedButton(text="إضافة عامل جديد", size_hint_y=None, height="48dp")
        add_button.bind(on_release=self.add_worker)
        main_layout.add_widget(add_button)
        
        # Workers List
        scroll = MDScrollView()
        self.workers_list = MDList()
        scroll.add_widget(self.workers_list)
        main_layout.add_widget(scroll)
        
        self.add_widget(main_layout)
        self.load_workers()

    def add_worker(self, instance):
        print("Add worker clicked")

    def load_workers(self):
        # Load workers from database
        for i in range(2):
            item = OneLineListItem(text=f"عامل {i+1}")
            self.workers_list.add_widget(item)

