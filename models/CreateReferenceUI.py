from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

from value import alfavit, numbers
from config import SMALL_WINDOW, BIG_WINDOW, FONT_INPUT_SIZE

class CreateReferenceUI(Screen):
    """окно создания нового обозначения"""
    
    font_input_size = FONT_INPUT_SIZE

    def on_enter(self):
        Window.size = SMALL_WINDOW

        self.ids.level1.text = ''
        self.ids.level2.text = ''
        self.ids.level3.text = ''
    
    def insert_level1(self,substring,from_undo=False):
        substring = substring.lower()
        if len(self.ids.level1.text) < 8:
            if substring in alfavit \
                or substring in numbers:
                self.ids.level1.text += substring


    def insert_level2(self,substring,from_undo=False):
        if len(self.ids.level2.text) < 8:
            if substring in numbers:
                self.ids.level2.text += substring

    def insert_level3(self,substring,from_undo=False):
        if len(self.ids.level3.text) < 3:
            if substring in numbers:
                self.ids.level3.text += substring


    def create_reference(self):
        pass

    def return_project(self):
        Window.size=BIG_WINDOW

        self.manager.transition.direction = 'right'
        self.manager.current = 'ProjectUI'


