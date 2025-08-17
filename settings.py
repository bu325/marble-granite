from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

class SettingsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "settings"
        self.build_ui()

    def build_ui(self):
        main_layout = MDBoxLayout(orientation="vertical", padding=20, spacing=10)
        
        # Title
        title = MDLabel(text="الإعدادات العامة", theme_text_color="Primary", 
                       size_hint_y=None, height="48dp", halign="center")
        main_layout.add_widget(title)
        
        # Content placeholder
        content = MDLabel(text="هنا ستكون إعدادات التطبيق.", halign="center")
        main_layout.add_widget(content)
        
        self.add_widget(main_layout)

