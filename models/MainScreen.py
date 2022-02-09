from kivy.uix.screenmanager import Screen
from value import USER
from functions import get_hello_start 

class MainScreen(Screen):
    def on_enter(self):
        self.ids.hello.text = get_hello_start() +  USER.first_name + '.'

    def logout(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LoginUI'
