from kivy.uix.screenmanager import Screen

from kivy.uix.button import Button
from functions import project_team_users, users_list, user_info
from value import VIEW_PROJECT 

class ProjectTeamUI(Screen):
    """Окно для редактирования пользователей
    входящих в команду проекта"""
    def on_enter(self):
        in_team = project_team_users (VIEW_PROJECT.p_name)
        
        self.update_users_in_team(in_team)
        users = users_list()
        for user in users:
            if user in in_team:
                users.remove(user)

        self.update_users_out_team(users)


    def update_users_in_team(self, in_team : list):
        "обновляет список юзеров в проекте"
        self.ids.users_in_team.clear_widgets()
        for user in in_team:
            button = Button(
                    text = str(user),
                    background_color = (0.32,0.32,0.32,1),
                    font_size = '0.635cm',
                    on_press = self.view_team_user
                    )
            self.ids.users_in_team.add_widget(button)

    def update_users_out_team(self, out_team : list):
        "Обновляет список юзеров вне проекта"
        self.ids.users_out_team.clear_widgets()
        for user in out_team:
            button = Button(
                    text = str(user),
                    background_color = (0.32,0.32,0.32,1),
                    font_size = '0.635cm',
                    on_press = self.view_out_team_user
                    )
            self.ids.users_out_team.add_widget(button)

    def view_team_user(self,instance):
        pass

    def view_out_team_user(self,instance):
        "Переход на окно добавления пользователя в команду"
        user_info(instance.text)
        self.manager.transition.direction = "left"
        self.manager.current = 'AddTeamUserUI'

    def return_project(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'ProjectUI'

