from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.button import Button


from functions import users_list, user_info
from config import SMALL_WINDOW, FONT_GRID_SIZE, FONT_TEXT_SIZE 

class UsersUI(Screen):
    """Класс окна в котором просматривать
    существующих юзеров"""
    
    font_text_size = FONT_TEXT_SIZE
    width = SMALL_WINDOW[0]

    def on_enter(self):
        Window.size = SMALL_WINDOW
        self.update_users_grid()
    
    def update_users_grid(self):
        "обновляет список кнопок с юзерами на экране"
        self.ids.users_grid.clear_widgets()
        for username in users_list():
            button = Button(
                    text = username,
                    background_color = (0.32,0.32,0.32,1),
                    font_size = FONT_GRID_SIZE,
                    on_press = self.view_user
                    )
            self.ids.users_grid.add_widget(button)

    def view_user(self,instance):
        "нажатие на кнопку с именем пользователя"
        user_info(instance.text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'ViewUserUI'

    def return_main(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'MainScreen'

    def add_user(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'NewUserUI'
