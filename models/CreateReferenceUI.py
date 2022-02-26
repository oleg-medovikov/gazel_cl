from kivy.uix.screenmanager import Screen


class CreateReferenceUI(Screen):
    """окно создания нового обозначения"""

    def on_enter(self):
        pass

    def create_reference(self):
        pass

    def return_project(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ProjectUI'


