from kivy.uix.screenmanager import Screen

from functions import create_project

class NewProjectUI(Screen):
    """Окно для создание нового проекта"""
    def on_enter(self):
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
