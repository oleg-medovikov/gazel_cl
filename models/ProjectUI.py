from kivy.uix.screenmanager import Screen

from kivy.uix.button import Button
from value import VIEW_PROJECT

from config import FONT_GRID_SIZE

class ProjectUI(Screen):
    """Окно работы с проектом"""

    def on_enter(self):
        self.ids.hello.text = f"Проект {VIEW_PROJECT.p_name}"
        self.ids.description.text = VIEW_PROJECT.p_description

        LEVEL1 = ['1','2','3']
        
        self.update_level1(LEVEL1)
    
    def update_level1(self, LEVEL1):
        "обновляет список кодов первого уровня"
        self.ids.level1.clear_widgets()
        self.ids.level2.clear_widgets()
        self.ids.level3.clear_widgets()


        for code in LEVEL1:
            button = Button(
                    text = str(code),
                    background_color = (0.32,0.32,0.32,1),
                    font_size = FONT_GRID_SIZE,
                    on_press = self.update_level2
                    )
            self.ids.level1.add_widget(button)

    def update_level2(self, instance):
        "обновляет список кодов второго уровня"
        self.ids.level2.clear_widgets()
        self.ids.level3.clear_widgets()

        LEVEL2 = ['1','2']

        for code in LEVEL2:
            button = Button(
                    text = str(code),
                    background_color = (0.32,0.32,0.32,1),
                    font_size = FONT_GRID_SIZE,
                    on_press = self.update_level3
                    )
            self.ids.level2.add_widget(button)

    def update_level3(self, instance):
        "обновляет список кодов третье уровня"
        self.ids.level3.clear_widgets()

        LEVEL3 = ['1','2','3','4']

        for code in LEVEL3:
            button = Button(
                    text = str(code),
                    background_color = (0.32,0.32,0.32,1),
                    font_size = FONT_GRID_SIZE,
                    on_press = self.view_reference
                    )
            self.ids.level3.add_widget(button)


    def view_reference(self, instance):
        pass
    
    def add_reference(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'CreateReferenceUI'

    def return_main(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'MainScreen'

    def view_team(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'ProjectTeamUI'
