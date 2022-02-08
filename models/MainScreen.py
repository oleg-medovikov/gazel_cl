from kivy.uix.screenmanager import Screen
from user import USER
from functions import get_hello_start 

class MainScreen(Screen):
    def on_enter(self):
        self.ids.hello.text = get_hello_start() +  USER.first_name + '.'
