from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

from kivy.uix.button import Button

from config import BIG_WINDOW, FONT_TEXT_SIZE, FONT_GRID_SIZE
from value import VIEW_REFERENCE, FILES_LIST
from functions import objects_list


class ReferenceUI(Screen):
    "Большое окно для работы с файлами внутри наименования"

    font_text_size = FONT_TEXT_SIZE
    width = BIG_WINDOW[0]

    def on_enter(self):
        Window.size=BIG_WINDOW

        self.ids.r_name.text = VIEW_REFERENCE.r_name

        objects_list()
        
        self.update_files_grid()
        

    def update_files_grid(self):
        "обновляет список доступных проектов"
        self.ids.files_grid.clear_widgets()
        for file in  FILES_LIST:
            button = Button(
                    text = file.name,
                    background_color = file.color,
                    font_size = FONT_GRID_SIZE
                    )
            self.ids.files_grid.add_widget(button)
 

    def return_project(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ProjectUI'



