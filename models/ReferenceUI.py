from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ListProperty, NumericProperty

import datetime, threading

from pathlib import Path
from config import BIG_WINDOW, FONT_TEXT_SIZE, FONT_GRID_SIZE
from value import VIEW_REFERENCE, FILES_LIST
from functions import objects_list, objects_create, \
        objects_load, objects_update, objects_delete 


class ReferenceUI(Screen):
    "Большое окно для работы с файлами внутри наименования"

    font_text_size = FONT_TEXT_SIZE
    width = BIG_WINDOW[0]

    CLOSE_IMG = Path('.', 'img', 'close.png')

    logi = ListProperty([])
    logi_len = NumericProperty(0)

    def  on_pre_enter(self):
        Window.size=BIG_WINDOW
        Window.minimum_width, Window.minimum_height = BIG_WINDOW

    def on_enter(self):
        self.ids.r_name.text = VIEW_REFERENCE.r_name

        objects_list()
        
        if len(FILES_LIST) == 0:
            self.ids.r_name.text += '\n\nУ данного обозначения ещё нет файлов'
        else:
            self.ids.r_name.text += '\n\nФайлы данного обозначения:'
        
        self.update_files_grid()
        self.add_log('Прочтены файлы в директории и базе', 'white')
    
    def on_logi(self,*args):
        "Обновляем список событий"
        if len(self.logi) != self.logi_len:
            self.ids.log_grid.add_widget(self.logi[-1])
            self.ids.log_scroll.scroll_to(self.logi[-1])
            self.logi_len = len(self.logi)

    def add_log(self, LOG, COLOR):
        label = Label(
                text = datetime.datetime.now().strftime('%H:%M:%S') +'   '+ LOG,
                font_size = FONT_GRID_SIZE,
                text_size =  [0.8*self.size[0] - 20, self.size[1]],
                color = COLOR,
                halign = 'left',
                valign = 'middle'
                )
        self.logi.append(label)

    def update_files_grid(self):
        "обновляет список доступных файлов"
        self.ids.files_grid.clear_widgets()
        for file in  FILES_LIST:
            button = Button(
                    text = f'[color=ffffff]{file.name}[/color]',
                    markup=True,
                    background_color = file.color,
                    opacity = '0.75',
                    font_size = FONT_GRID_SIZE,
                    text_size =  [0.375*self.size[0], self.size[1]],
                    halign = 'left',
                    valign = 'middle',
                    on_press = self.view_file
                    )
            button.id = file.name
            self.ids.files_grid.add_widget(button)

            label = Label(
                    font_size = FONT_GRID_SIZE,
                    markup=True,
                    size_hint_x = None,
                    width =  '4cm',
                    text = f'[color=ffffff]{file.type}[/color]',
                    #text = file.type,
                    )
            self.ids.files_grid.add_widget(label)

            button = Button(
                    background_normal = self.CLOSE_IMG.as_posix(),
                    size_hint_x = None,
                    width = '1.5cm',
                    on_press = self.delete_file
                    )

            button.id = file.id
            self.ids.files_grid.add_widget(button)

    def view_file(self,instance):
        objects_list()
        self.update_files_grid()
    
    def delete_file(self,instance):
        if instance.id == '':
            return 1
        res = objects_delete(instance.id)

        if 'error' in res:
            self.add_log(res['error'], 'darkred')
        elif "message" in res:
            self.add_log(res['message'], 'white')
        
        objects_list()
        self.update_files_grid()

#    def start_synchronization(self):
#       threading.Thread(target=self.synchronization).start() 

    def synchronization(self):
        self.add_log('Начинаю синхронизацию', 'white')

        for file in FILES_LIST:
            
            if   file.type == 'Новый':
                res = objects_create(FILES_LIST.index(file))
            
            elif file.type == 'Скачать':
                res = objects_load(FILES_LIST.index(file))
            
            elif file.type == 'Изменён':
                res = objects_update(FILES_LIST.index(file))
            
            elif file.type == 'Актуален':
                continue

            if 'error' in res:
                self.add_log(file.name + ' ' + res['error'], 'darkred')
            elif "message" in res:
                self.add_log(file.name + ' ' + res['message'], 'white')

        objects_list()
        self.update_files_grid()
        self.add_log('Закончил синхронизацию', 'white')
       # self.ids.load_files.background_normal = ''
       # self.ids.load_files.background_color = 'grey'


    def return_project(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ProjectUI'



