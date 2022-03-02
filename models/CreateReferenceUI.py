from kivy.uix.screenmanager import Screen

from value import alfavit, numbers

class CreateReferenceUI(Screen):
    """окно создания нового обозначения"""

    def on_enter(self):
        self.ids.level1.text = ''
    
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
        self.manager.transition.direction = 'right'
        self.manager.current = 'ProjectUI'


