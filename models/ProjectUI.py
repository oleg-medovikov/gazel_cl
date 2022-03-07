from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from value import VIEW_PROJECT

from config import FONT_GRID_SIZE, SMALL_WINDOW, BIG_WINDOW, \
                   FONT_TEXT_SIZE

class ProjectUI(Screen):
    """Большое окно работы с проектом"""

    font_text_size = FONT_TEXT_SIZE
    width = BIG_WINDOW[0]

    def on_enter(self):
        Window.size=BIG_WINDOW

        DESCRIPTION = f"Проект {VIEW_PROJECT.p_name}\n"
        DESCRIPTION += VIEW_PROJECT.p_description
        DESCRIPTION += "\n\nВыберете обозначение из доступных кодов"
        self.ids.description.text = DESCRIPTION
        

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
        Window.size = SMALL_WINDOW
        self.manager.transition.direction = 'left'
        self.manager.current = 'CreateReferenceUI'

    def return_main(self):
        self.ids.level1.clear_widgets()
        self.ids.level2.clear_widgets()
        self.ids.level3.clear_widgets()
        self.ids.description.text = ''

        Window.size = SMALL_WINDOW
        self.manager.transition.direction = 'right'
        self.manager.current = 'MainScreen'

    def view_team(self):
        Window.size = SMALL_WINDOW
        self.manager.transition.direction = 'up'
        self.manager.current = 'ProjectTeamUI'
