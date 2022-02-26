from kivy.uix.screenmanager import Screen

from value import VIEW_USER, VIEW_PROJECT
 
from functions import project_remove_user

class RemoveTeamUserUI(Screen):
    "Удаление пользователя из команды"
    def on_enter(self):
        if VIEW_USER.admin:
            admin = 'Является админом'
        else:
            admin = 'Является обычным пользователем'
        
        text = f"""Пользователь:
{VIEW_USER.username}
———————————————
ФИО:
{VIEW_USER.second_name} {VIEW_USER.first_name}
———————————————
Должность:
{VIEW_USER.position}
———————————————
{admin}"""
        self.ids.description.text = text
        self.ids.message.text = ''

    def return_project_team(self):
        self.manager.transition.direction = "right"
        self.manager.current = 'ProjectTeamUI'

    def remove_user_from_team(self):
        res = project_remove_user(
                VIEW_PROJECT.p_name,
                VIEW_USER.username
                )
        
        self.ids.message.text = res
