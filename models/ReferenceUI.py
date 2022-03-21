from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

from kivy.uix.button import Button

from config import BIG_WINDOW, FONT_TEXT_SIZE, FONT_GRID_SIZE
from value import VIEW_REFERENCE, FILES_LIST
from functions import objects_list, objects_create


class ReferenceUI(Screen):
    "Большое окно для работы с файлами внутри наименования"

    font_text_size = FONT_TEXT_SIZE
    width = BIG_WINDOW[0]

    def on_enter(self):
        Window.size=BIG_WINDOW

        self.ids.r_name.text = VIEW_REFERENCE.r_name

        objects_list()
        
        if len(FILES_LIST) == 0:
            self.ids.r_name.text += '\nУ данного обозначения еще нет файлов'
        else:
            self.ids.r_name.text += '\nФайлы данного обозначения:'
        
        self.update_files_grid()
        

    def update_files_grid(self):
        "обновляет список доступных файлов"
        self.ids.files_grid.clear_widgets()
        for file in  FILES_LIST:
            button = Button(
                    text = file.name +'   '+ file.type,
                    background_color = file.color,
                    font_size = FONT_GRID_SIZE,
                    on_press = self.view_file
                    )
            button.id = file.name
            self.ids.files_grid.add_widget(button)
 
    def view_file(self,instance):
        pass

    def synchronization(self):
        for file in FILES_LIST:
            if file.type == 'Не загружен в базу':
                res = objects_create(FILES_LIST.index(file))
                #print(res)

    def return_project(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ProjectUI'



