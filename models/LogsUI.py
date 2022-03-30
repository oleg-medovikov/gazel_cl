from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label

from value import VIEW_PROJECT, VIEW_LOGS, VIEW_LOGS_DATES
from functions import logs_list

from config import FONT_GRID_SIZE, BIG_WINDOW, FONT_TEXT_SIZE

class LogsUI(Screen):
    "Большое окно с логами"

    font_text_size = FONT_TEXT_SIZE
    width = BIG_WINDOW[0]

    def on_enter(self):
        Window.size=BIG_WINDOW

        DESCRIPTION = f"Проект {VIEW_PROJECT.p_name}\n"
        self.ids.description.text = DESCRIPTION

        logs_list(VIEW_PROJECT.p_id)

        self.update_dates_grid()

        if len(VIEW_LOGS):
            self.update_logs_grid(VIEW_LOGS_DATES[0])


    def update_dates_grid(self):
        "Обновляем список кнопочек с датами"
        self.ids.dates_grid.clear_widgets()
        self.ids.dates_grid.cols = len(VIEW_LOGS_DATES)
        if len(VIEW_LOGS_DATES) == 0:
            self.ids.description.text += '\nНет логов'
            return 1
        else:
            self.ids.description.text += '\nДоступные даты:'

        for date in VIEW_LOGS_DATES:
            button =Button(
                        text = date,
                        size_hint_x = None,
                        size_hint_y = None,
                        width = '3.75cm',
                        height = '0.75cm',
                        background_color = (0.32,0.32,0.32,1),
                        font_size = FONT_GRID_SIZE,
                        on_press = self.see_log_by_date
                            )
            self.ids.dates_grid.add_widget(button)

    def see_log_by_date(self, instance):
        "нажатие на дату"
        self.update_logs_grid(instance.text)

    def update_logs_grid(self, DATE):
        "Обновляем таблицу с логами за дату" 
        self.ids.logs_grid.clear_widgets()
        FONT_SIZE = '0.4cm'

        for log in VIEW_LOGS:
            if log.date == DATE:
                TIME = Label(
                    font_size = FONT_SIZE,
                     markup=True,
                     text = f'[color=000000][b]{log.time[:-3]}[/b][/color]',
                     size_hint = (0.14,1),
                     halign = 'left'
                        )
                USER = Label(
                    font_size = FONT_SIZE,
                    markup=True,
                    size_hint = (0.30,1),
                    halign = 'left',
                    text = f'[color=000000][b]{log.username}[/b]\n[/color][color=ffffff]{log.user}[/color]',
                        )
                REF = Label(
                    font_size = FONT_SIZE,
                    markup=True,
                    size_hint = (0.2,1),
                    halign = 'left',
                    text = f'[color=ffffff]{log.r_code}[/color]',
                        )
                EVENT = Label(
                    font_size = FONT_SIZE,
                    markup=True,
                    size_hint = (0.55,1),
                    text_size = (0.55*self.width, self.height),
                    halign = 'left',
                    valign = "middle",
                    text = f'[color=ffffff]{log.event}[/color]',
                        )
                self.ids.logs_grid.add_widget(TIME)
                self.ids.logs_grid.add_widget(USER)
                self.ids.logs_grid.add_widget(REF)
                self.ids.logs_grid.add_widget(EVENT)

    def return_project(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'ProjectUI'

    def refresh(self):
        pass



