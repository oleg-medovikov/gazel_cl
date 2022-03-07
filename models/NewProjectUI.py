from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

from config import SMALL_WINDOW, FONT_TEXT_SIZE, FONT_INPUT_SIZE
from functions import create_project

class NewProjectUI(Screen):
    """Окно для создание нового проекта"""
    font_input_size = FONT_INPUT_SIZE
    font_text_size = FONT_TEXT_SIZE
    width = SMALL_WINDOW[0]

    def on_enter(self):
        Window.size = SMALL_WINDOW
        self.ids.project_name.text = ""
        self.ids.description.text = ""
        self.ids.message.text = "Задайте имя нового проекта"

    def add_project(self):
        if self.ids.project_name.text == "":
            self.ids.message.text = "Имя проекта не может быть пустым!"
            return 1
        elif self.ids.description.text == "":
            self.ids.message.text = "Не оставляйте проект без описания!"
            return 1
        else:
            P_NAME = self.ids.project_name.text
            P_DESCRIPTION = self.ids.description.text

            self.ids.message.text = create_project(P_NAME,P_DESCRIPTION)
            return 1

    def return_main(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'MainScreen'
