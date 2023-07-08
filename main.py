from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        return (
            MDScreen(
                MDRectangleFlatButton(
                    text="Hello, Worldcgvfddfdfgfgff!!!!!!",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
            )
        )

#dfghgfh
MainApp().run()
