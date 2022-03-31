from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.button import Button

from value import USER
from functions import get_hello_start, projects_list, project_info
from config import SMALL_WINDOW, BIG_WINDOW, FONT_GRID_SIZE, \
                   FONT_TEXT_SIZE


class MainScreen(Screen):
    """Главное окно с выбором проекта
    и с переходом на редактирование пользователей"""
    font_text_size = FONT_TEXT_SIZE
    width = SMALL_WINDOW[0]

    def on_pre_enter(self):
        Window.size=SMALL_WINDOW
        Window.minimum_width, Window.minimum_height = Window.size
       
    def on_enter(self):
        self.ids.hello.text = get_hello_start() +  USER.first_name + '.' \
                + "\nВыберите из доступных проектов:" 

        self.update_projects_grid()

    def update_projects_grid(self):
        "обновляет список доступных проектов"
        self.ids.projects_grid.clear_widgets()
        for project in projects_list():
            button = Button(
                    text = project,
                    background_color = (0.32,0.32,0.32,1),
                    font_size = FONT_GRID_SIZE,
                    on_press = self.view_project
                    )
            self.ids.projects_grid.add_widget(button)
        
        if USER.admin:
            #админу дополнительная кнопка для добавления проекта
            button = Button(
                    text = "Добавить проект",
                    background_color = (0.32,0.32,0.32,1),
                    font_size = FONT_GRID_SIZE,
                    on_press = self.add_project
                    )
            self.ids.projects_grid.add_widget(button)

    def view_project(self,instance):
        "нажатие на кнопку с именем проекта"
        project_info(instance.text)
        Window.size=BIG_WINDOW

        self.manager.transition.direction = 'left'
        self.manager.current = 'ProjectUI'

    def add_project(self,instance):
        "нажатие на кнопку добавления проекта"
        self.manager.transition.direction = 'left'
        self.manager.current = 'NewProjectUI'

    def logout(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LoginUI'

    def see_users(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'UsersUI'
