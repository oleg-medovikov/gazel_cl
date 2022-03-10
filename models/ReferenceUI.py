from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

from config import BIG_WINDOW, FONT_TEXT_SIZE
from value import VIEW_REFERENCE



class ReferenceUI(Screen):
    "Большое окно для работы с файлами внутри наименования"

    font_text_size = FONT_TEXT_SIZE
    width = BIG_WINDOW[0]

    def on_enter(self):
        Window.size=BIG_WINDOW



    def return_project(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ProjectUI'



