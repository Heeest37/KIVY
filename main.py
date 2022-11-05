from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.tab import MDTabsBase
from kivymd.font_definitions import fonts
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFloatingActionButton

KV = '''
MDScreen:

    MDRaisedButton:
        id: button
        text: "PRESS ME"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.menu.open()
'''

class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class Tab(MDFloatLayout, MDTabsBase):
    pass

class MapApp(MDApp):
    title = 'Карта школы №22'
    by_who = 'Автор: Соболев Александр'





    def build(self):
        return Builder.load_file('C:/Users/User/PycharmProjects/KIVY/my.kv')


    def on_start(self):
        icons_item_menu_lines = {
            "home": "Главная",
            "numeric-1-box": "Этаж 1",
            "numeric-2-box": "Этаж 2",
            "numeric-3-box": "Этаж 3",
            "numeric-4-box": "Этаж 4",
            "alert-circle": "О приложении",
            "shield-sun": "Тёмная/Светлая",
        }
        icons_item_menu_tabs = {
            "calculator-variant": "Input",  # ab-testing
            "table-large": "Table",
            "chart-areaspline": "Graph",
            "chart-pie": "Chart",  # chart-arc
            "book-open-variant": "Sum",
        }
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )
        #for icon_name, name_tab in icons_item_menu_tabs.items():
         #   self.root.ids.tabs.add_widget(
          #      Tab(
           #         title=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/size][/font] {name_tab}"
            #    )
            #)



    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''
        Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        count_icon = instance_tab.icon  # get the tab icon
        print(f"Welcome to {count_icon}' tab'")

    def on_star_click(self):
        pass


MapApp().run()