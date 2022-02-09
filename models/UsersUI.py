from kivy.uix.screenmanager import Screen

class UsersUI(Screen):
    """Класс окна в котором просматривать
    существующих юзеров"""
    #def on_enter(self):
    #    pass

    def return_main(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'MainScreen'

    def add_user(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'NewUserUI'
