import platform, os, sys
from pathlib import Path

#os.environ['KIVY_NO_CONSOLELOG'] = '1'

os.environ['USE_SDL2'] = '1'

if platform.system() == 'Windows':
    os.environ['USE_SDL2'] = '1'

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.resources import resource_add_path, resource_find

from models import LoginUI, MainScreen, UsersUI, NewUserUI, ViewUserUI, NewProjectUI
from models import ProjectUI, ProjectTeamUI, AddTeamUserUI, RemoveTeamUserUI
from models import CreateReferenceUI, ReferenceUI, LogsUI

from config import SMALL_WINDOW
from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '700')

# На случай если есть прокси ======
import httplib2
pi = httplib2.proxy_info_from_environment()
if pi:
    import socks
    socks.setdefaultproxy(pi.proxy_type, pi.proxy_host, pi.proxy_port)
    socks.wrapmodule(httplib2)

httplib2.Http()
#====================================

KV_PATH = Path('.', 'kv')
KV_FILES = list(KV_PATH.glob('*.kv'))

STRING = ''
for file in KV_FILES:
    STRING += open(file, 'r', encoding='utf-8').read()

Builder.load_string(STRING)

class Gazel_cl(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginUI           (name = 'LoginUI'))
        sm.add_widget(MainScreen        (name = 'MainScreen'))
        sm.add_widget(UsersUI           (name = 'UsersUI'))
        sm.add_widget(NewUserUI         (name = 'NewUserUI'))
        sm.add_widget(ViewUserUI        (name = 'ViewUserUI'))
        sm.add_widget(NewProjectUI      (name = 'NewProjectUI'))
        sm.add_widget(ProjectUI         (name = 'ProjectUI'))
        sm.add_widget(ProjectTeamUI     (name = 'ProjectTeamUI'))
        sm.add_widget(AddTeamUserUI     (name = 'AddTeamUserUI'))
        sm.add_widget(RemoveTeamUserUI  (name = 'RemoveTeamUserUI'))
        sm.add_widget(CreateReferenceUI (name = 'CreateReferenceUI'))
        sm.add_widget(ReferenceUI       (name = 'ReferenceUI'))
        sm.add_widget(LogsUI            (name = 'LogsUI'))
        return sm
    
if __name__ == '__main__':
    app = Gazel_cl()
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    app.run()

