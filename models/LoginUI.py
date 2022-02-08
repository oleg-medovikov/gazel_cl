from kivy.uix.screenmanager import Screen

from functions import login

class LoginUI(Screen):
    "Класс первого окна входа"
    def try_log_in(self):
        "попытка залогиниться при нажатии кнопки"
        res = login(self.ids.username.text,self.ids.password.text)
        if not res[0]:
            self.ids.error.text = res[1] 
        else:
            self.manager.transition.direction = "left"
            self.manager.current = 'MainScreen'


