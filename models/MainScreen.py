from kivy.uix.screenmanager import Screen
from value import USER
from functions import get_hello_start 

class MainScreen(Screen):
    def on_enter(self):
        print(USER.token)
        self.ids.hello.text = get_hello_start() +  USER.first_name + '.'

    def logout(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LoginUI'

    def see_users(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'UsersUI'
