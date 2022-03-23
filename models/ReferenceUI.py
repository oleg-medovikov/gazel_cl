from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

from kivy.uix.button import Button
from kivy.uix.label import Label

import datetime 
from config import BIG_WINDOW, FONT_TEXT_SIZE, FONT_GRID_SIZE
from value import VIEW_REFERENCE, FILES_LIST
from functions import objects_list, objects_create, objects_load


class ReferenceUI(Screen):
    "Большое окно для работы с файлами внутри наименования"

    font_text_size = FONT_TEXT_SIZE
    width = BIG_WINDOW[0]

    def on_enter(self):
        Window.size=BIG_WINDOW

        self.ids.r_name.text = VIEW_REFERENCE.r_name

        objects_list()
        
        if len(FILES_LIST) == 0:
            self.ids.r_name.text += '\n\nУ данного обозначения ещё нет файлов'
        else:
            self.ids.r_name.text += '\n\nФайлы данного обозначения:'
        
        self.update_files_grid()
        self.update_log_grid('Прочтены файлы в директории и базе', 'white')

    def update_log_grid(self, LOG, COLOR):
        "Обновляем список событий"
        label = Label(
                text = datetime.datetime.now().strftime('%H:%M:%S') +'   '+ LOG,
                font_size = FONT_GRID_SIZE,
                text_size =  [0.8*self.size[0] - 20, self.size[1]],
                color = COLOR,
                halign = 'left',
                valign = 'middle'
                )
        self.ids.log_grid.add_widget(label)
        self.ids.log_scroll.scroll_to(label)

    def update_files_grid(self):
        "обновляет список доступных файлов"
        self.ids.files_grid.clear_widgets()
        for file in  FILES_LIST:
            button = Button(
                    text = file.name +'   '+ file.type,
                    background_color = file.color,
                    font_size = FONT_GRID_SIZE,
                    text_size =  [0.75*self.size[0], self.size[1]],
                    halign = 'left',
                    valign = 'middle',
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
            elif file.type == 'Готов к загрузке':
                res = objects_load(FILES_LIST.index(file))
            elif file.type == 'Не требует синхронизации':
                continue

            if 'error' in res:
                self.update_log_grid(file.name + ' ' + res['error'], 'darkred')
            elif "message" in res:
                self.update_log_grid(file.name + ' ' + res['message'], 'white')
 
        objects_list()
        self.update_files_grid()

    def return_project(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ProjectUI'



