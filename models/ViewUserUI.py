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
        
        text = f"""Информация о пользователе: \n{VIEW_USER.username},
        \n {VIEW_USER.second_name} {VIEW_USER.first_name}
        \n Находится в должности: \n {VIEW_USER.position}.
        \n {admin}
        """
        self.ids.description.text = text

    def return_users(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'UsersUI'
