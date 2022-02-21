from kivy.uix.screenmanager import Screen

from value import VIEW_PROJECT

class ProjectUI(Screen):
    """Окно работы с проектом"""
    def on_enter(self):
        self.ids.hello.text = f"Проект {VIEW_PROJECT.p_name}"
        self.ids.description.text = VIEW_PROJECT.p_description

    def return_main(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'MainScreen'

    def view_team(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'ProjectTeamUI'
