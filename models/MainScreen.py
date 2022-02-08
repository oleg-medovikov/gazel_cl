from kivy.uix.screenmanager import Screen

from config import USER_FIRST_NAME, USER_TOKEN

class MainScreen(Screen):
    def on_enter(self):
        self.ids.hello.text = "Добрый " +  USER_FIRST_NAME 
