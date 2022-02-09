from kivy.uix.screenmanager import Screen
from value import User
from functions import create_user

class NewUserUI(Screen):
    """Класс окна в котором просматривать
    существующих юзеров"""
    #def on_enter(self):
    #    pass

    def return_users(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'UsersUI'

    def add_user(self):
        if self.ids.password1.text != self.ids.password2.text:
            self.ids.message.text = 'Пароли не совпадают'
            return 1
        elif self.ids.username.text == '':
            self.ids.message.text = 'Придумайте удобный username'
            return 1
        elif self.ids.first_name.text =='':
            self.ids.message.text = 'Внесите имя и отчество'
            return 1
        elif self.ids.second_name.text == '':
            self.ids.message.text = 'Внесите фамилию'
            return 1
        elif self.ids.position.text == '':
            self.ids.message.text = 'Напишите должность'
            return 1
        else:
            new_user = User()
            new_user.first_name = self.ids.first_name.text
            new_user.second_name = self.ids.second_name.text
            new_user.username = self.ids.username.text
            new_user.password_hash = self.ids.password1.text
            new_user.position = self.ids.first_name.text
            new_user.admin = False
            
            res = create_user(new_user)
            
            if not res[0]:
                "Выводим ошибку при провале"
                self.ids.message.text = res[1]
            else:
                self.ids.message.text = res[1]


            
