from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from value import VIEW_PROJECT, VIEW_REFERENCE

from functions import reference_level1, reference_level2, \
        reference_level3, reference_name
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
        
        LEVEL1 = reference_level1()
        if len(LEVEL1):
            DESCRIPTION += "\n\nВыберете обозначение из доступных кодов"
        else:
            DESCRIPTION += "\n\nДанный проект ещё пустой, создайте новые обозначения"

        self.ids.description.text = DESCRIPTION
        
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

        VIEW_REFERENCE.r_level1 = instance.text

        LEVEL2 = reference_level2()

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

        VIEW_REFERENCE.r_level2 = instance.text

        LEVEL3 = reference_level3()

        for code in LEVEL3:
            button = Button(
                    text = str(code),
                    background_color = (0.32,0.32,0.32,1),
                    font_size = FONT_GRID_SIZE,
                    on_press = self.view_reference
                    )
            self.ids.level3.add_widget(button)


    def view_reference(self, instance):
        "Переходим в окно наименования"
        VIEW_REFERENCE.r_level3 = instance.text
        reference_name()
        self.manager.transition.direction = 'left'
        self.manager.current = 'ReferenceUI'
    
    def add_reference(self):
        Window.size = SMALL_WINDOW
        self.manager.transition.direction = 'left'
        self.manager.current = 'CreateReferenceUI'
    
    def view_logs(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'LogsUI'

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
