from kivy.uix.screenmanager import Screen

from functions import create_project

from value import Project, USER

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
            new_project = Project()
            new_project.token = USER.token
            new_project.p_name = self.ids.project_name.text
            new_project.p_description = self.ids.description.text

            self.ids.message.text = create_project(new_project)
            return 1

    def return_main(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'MainScreen'
