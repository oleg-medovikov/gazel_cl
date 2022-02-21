from kivy.uix.screenmanager import Screen

from kivy.uix.button import Button
from functions import project_team_users
from value import VIEW_PROJECT

class ProjectTeamUI(Screen):
    """Окно для редактирования пользователей
    входящих в команду проекта"""
    def on_enter(self):
        in_team = project_team_users (VIEW_PROJECT.p_name)
        
        self.update_users_in_team(in_team)

    def update_users_in_team(self, in_team: list):
        "обновляет список юзеров в проекте"
        self.ids.users_in_team.clear_widgets()
        for user in in_team:
            print(user)
            button = Button(
                    text = str(user),
                    background_color = (0.32,0.32,0.32,1),
                    font_size = '0.635cm',
                    on_press = self.view_team_user
                    )
            self.ids.users_in_team.add_widget(button)

    def update_users_out_team(self):
        pass

    def view_team_user(self,instance):
        pass

    def return_project(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'ProjectUI'

