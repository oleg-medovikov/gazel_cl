from kivy.uix.screenmanager import Screen
from kivy.core.window import Window 

from value import VIEW_USER, VIEW_PROJECT
 
from functions import project_add_user

class AddTeamUserUI(Screen):
    "Добавление пользователя в команду"
    def on_enter(self):
        Window.size=(375,700)
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
        self.ids.slider.value = -3

    def slider_value_change(self,value):
        if value == 0:
            message = "0 Полные права на проект"
        elif value == -1:
            message = "1 Доступ к добавлению новых файлов"
        elif value == -2:
            message = "2 Доступ только на загрузку файлов"
        elif value == -3:
            message = "3 Доступ только для просмотра"

        self.ids.access.text = message

    def return_project_team(self):
        self.manager.transition.direction = "right"
        self.manager.current = 'ProjectTeamUI'

    def add_user_to_team(self):
        res = project_add_user(
                VIEW_PROJECT.p_name,
                VIEW_USER.username,
                -self.ids.slider.value
                )
        
        self.ids.access.text = res


