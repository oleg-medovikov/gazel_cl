from kivy.uix.screenmanager import Screen

from functions import update_password
from value import VIEW_USER 

class ViewUserUI(Screen):
    """ Окно в котором рассматриваем параметры
    конкретного пользователя и меняем пароль"""

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
        
        self.ids.error.text = ""
        self.ids.password1.text = ""
        self.ids.password2.text = ""

    def password_update(self):
        if self.ids.password1.text == "" :
            self.ids.error.text = "Введите новый пароль!"
        elif self.ids.password1.text != self.ids.password2.text:
            self.ids.error.text = "Пароли не совпадают!"
        else:
            res = update_password(self.ids.password1.text)
            self.ids.error.text = res

    def return_users(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'UsersUI'
