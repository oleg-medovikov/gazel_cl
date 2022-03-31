from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import cm

from value import VIEW_PROJECT, VIEW_LOGS, VIEW_LOGS_DATES
from functions import logs_list

from config import FONT_GRID_SIZE, BIG_WINDOW, FONT_TEXT_SIZE

class LogsUI(Screen):
    "Большое окно с логами"

    font_text_size = FONT_TEXT_SIZE
    width = BIG_WINDOW[0]

    def on_pre_enter(self):
        Window.size=BIG_WINDOW
        Window.minimum_width, Window.minimum_height = Window.size

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
        FONT_SIZE = '0.375cm'

        for log in VIEW_LOGS:
            if log.date == DATE:
                TIME = Label(
                    font_size = FONT_SIZE,
                    markup=True,
                    text = f'[color=000000][b]{log.time[:-3]}[/b][/color]',
                    size_hint = (None,0.1),
                    width = cm(1.5),
                    text_size = (cm(1.5), cm(1.5)),
                    halign = "center",
                    valign = "middle",
                         )
                USER = Label(
                    font_size = FONT_SIZE,
                    markup=True,
                    size_hint = (None,1),
                    width = cm(3.5),
                    text_size = (cm(3.5), cm(1.5)),
                    halign = 'left',
                    valign = "top",
                    text = f'[color=000000][b]{log.username}[/b]\n[/color][color=ffffff]{log.user}[/color]',
                        )

                EVENT = Label(
                    font_size = FONT_SIZE,
                    markup=True,
                    size_hint = (None,1),
                    width = cm(5),
                    text_size = (cm(4.8), cm(1.5)),
                    halign = 'left',
                    valign = "top",
                    text = f'[color=ffffff]{log.event}[/color]',
                        )

                if log.r_code is None:
                    REF_TEXT = ''
                else:
                    REF_TEXT = log.r_code

                REF = Label(
                    font_size = FONT_SIZE,
                    markup=True,
                    size_hint = (None,1),
                    width = cm(2),
                    text_size = (cm(2), cm(1.5)),
                    halign = 'left',
                    valign = "top",
                    text = f'[color=ffffff]{REF_TEXT}[/color]',
                        )
                self.ids.logs_grid.add_widget(TIME)
                self.ids.logs_grid.add_widget(USER)
                self.ids.logs_grid.add_widget(EVENT)
                self.ids.logs_grid.add_widget(REF)

    def return_project(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'ProjectUI'

    def refresh(self):
        pass



