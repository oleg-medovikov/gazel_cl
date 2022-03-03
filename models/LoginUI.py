from kivy.uix.screenmanager import Screen

from functions import login
from config import DEFAULT_USERNAME, DATABASE_URL
from value import to_latin

class LoginUI(Screen):
    "Класс первого окна входа"
    def on_enter(self):
        self.ids.password.text = ""

        if  DATABASE_URL != '': 
            self.ids.username.text = DEFAULT_USERNAME
            self.ids.error.text = "Аутентификация"
        else:
            self.ids.error.text = "Не найден config.cfg!"

    def insert_text(self, substring, from_undo=False):
        s = substring.translate(to_latin)
        self.ids.username.text += s

    def try_log_in(self):
        "попытка залогиниться при нажатии кнопки"
        if DATABASE_URL != '':
            res = login(self.ids.username.text,self.ids.password.text)
            if not res[0]:
                "Выводим ошибку при провале"
                self.ids.error.text = res[1] 
            else:
                self.manager.transition.direction = "left"
                self.manager.current = 'MainScreen'
        else:
            pass

