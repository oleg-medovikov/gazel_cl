from kivy.uix.screenmanager import Screen
from value import User, to_latin
from functions import create_user

class NewUserUI(Screen):
    """Класс окна в котором просматривать
    существующих юзеров"""
    #def on_enter(self):
    #    pass

    def return_users(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'UsersUI'

    def insert_text(self, substring, from_undo=False):
        s = substring.translate(to_latin)
        self.ids.username.text += s

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
            
            first_name = self.ids.first_name.text
            second_name = self.ids.second_name.text
            username = self.ids.username.text
            password = self.ids.password1.text
            position = self.ids.position.text
            admin = False
            
            res = create_user(
                    first_name,
                    second_name,
                    username,
                    password,
                    position,
                    admin
                    )
            
            if not res[0]:
                "Выводим ошибку при провале"
                self.ids.message.text = res[1]
            else:
                self.ids.message.text = res[1]


            
