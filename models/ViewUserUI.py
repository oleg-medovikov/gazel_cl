from kivy.uix.screenmanager import Screen

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

    def update_password(self):
        if self.ids.password1.test != "" :
            self.ids.error.text = "Введите новый пароль!"
        elif self.ids.password1.test != self.ids.password2.text:
            self.ids.error.text = "Пароли не совпадают!"
        else:
            res = password_update(self.ids.password1.text)

    def return_users(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'UsersUI'
