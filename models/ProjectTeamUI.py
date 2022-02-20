from kivy.uix.screenmanager import Screen

from kivy.uix.button import Button

class ProjectTeamUI(Screen):
    """Окно для редактирования пользователей
    входящих в команду проекта"""
    def on_enter(self):
        pass

    def update_users_in_team(self):
        pass

    def update_users_out_team(self):
        pass

    def return_project(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'ProjectUI'

