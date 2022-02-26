from kivy.uix.screenmanager import Screen

from functions import login
from config import DEFAULT_USERNAME
from value import to_latin

class LoginUI(Screen):
    "Класс первого окна входа"
    def on_enter(self):
        if not DEFAULT_USERNAME == "": 
            self.ids.username.text = DEFAULT_USERNAME
        self.ids.password.text = ""
        self.ids.error.text = "Аутентификация"

    def insert_text(self, substring, from_undo=False):
        s = substring.translate(to_latin)
        self.ids.username.text += s

    def try_log_in(self):
        "попытка залогиниться при нажатии кнопки"
        res = login(self.ids.username.text,self.ids.password.text)
        if not res[0]:
            "Выводим ошибку при провале"
            self.ids.error.text = res[1] 
        else:
            self.manager.transition.direction = "left"
            self.manager.current = 'MainScreen'


