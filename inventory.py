from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.scrollview import MDScrollView

class InventoryScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "inventory"
        self.build_ui()

    def build_ui(self):
        main_layout = MDBoxLayout(orientation="vertical", padding=20, spacing=10)
        
        # Title
        title = MDLabel(text="إدارة المخزون", theme_text_color="Primary", 
                       size_hint_y=None, height="48dp", halign="center")
        main_layout.add_widget(title)
        
        # Add Material Button
        add_button = MDRaisedButton(text="إضافة مادة جديدة", size_hint_y=None, height="48dp")
        add_button.bind(on_release=self.add_material)
        main_layout.add_widget(add_button)
        
        # Materials List
        scroll = MDScrollView()
        self.materials_list = MDList()
        scroll.add_widget(self.materials_list)
        main_layout.add_widget(scroll)
        
        self.add_widget(main_layout)
        self.load_materials()

    def add_material(self, instance):
        # This would open a dialog or navigate to an add material screen
        print("Add material clicked")

    def load_materials(self):
        # This would load materials from the database
        # For now, we'll add some dummy items
        for i in range(5):
            item = OneLineListItem(text=f"مادة {i+1}")
            self.materials_list.add_widget(item)

