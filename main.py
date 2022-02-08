from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder

from models import LoginUI, MainScreen 

Builder.load_string(f"""
{open('kv/login.kv', 'r').read()}
{open('kv/mainscreen.kv', 'r').read()}
""")


class Gazel_cl(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginUI(name = 'LoginUI'))
        sm.add_widget(MainScreen(name = 'MainScreen'))
        return sm
    
    
if __name__ == '__main__':
    app = Gazel_cl()
    Window.size=(400,700)
    app.run()
