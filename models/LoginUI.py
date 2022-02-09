from kivy.uix.screenmanager import Screen

from functions import login
from config import DEFAULT_USERNAME

class LoginUI(Screen):
    "Класс первого окна входа"
    def on_enter(self):
        if not DEFAULT_USERNAME == "": 
            self.ids.username.text = DEFAULT_USERNAME
        self.ids.password.text = ""

    def try_log_in(self):
        "попытка залогиниться при нажатии кнопки"
        res = login(self.ids.username.text,self.ids.password.text)
        if not res[0]:
            self.ids.error.text = res[1] 
        else:
            self.manager.transition.direction = "left"
            self.manager.current = 'MainScreen'


