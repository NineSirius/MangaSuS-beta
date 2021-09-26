from kivymd.app import MDApp
from kivy.lang import Builder


class Test(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'MangaSus'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Главная'
            icon: 'home'

            MDCard:
                size_hint: None, None
                size: "280dp", "180dp"
                pos_hint: {"center_x": .5, "center_y": .5}

                MDLabel:
                    text: "Токийские мсимим"
                    theme_text_color: "Secondary"
                    adaptive_height: True

                MDSeparator:
                    height: "1dp"

                MDLabel:
                    text: "Body"

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Меню'
            icon: 'view-grid'

            MDLabel:
                text: 'Меню'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Профиль'
            icon: 'account-circle'

            MDLabel:
                text: 'Профиль'
                halign: 'center'
'''
        )

class TestCard(MDApp):
    def build(self):
        return Builder.load_string(KV)

Test().run()