from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder

from models import LoginUI, MainScreen, UsersUI, NewUserUI, ViewUserUI, NewProjectUI
from models import ProjectUI, ProjectTeamUI, AddTeamUserUI, RemoveTeamUserUI
from models import CreateReferenceUI
import platform, os


if platform.system() == 'Windows':
    os.environ['KIVY_NO_CONSOLELOG'] = '1'
    os.environ['USE_SDL2'] = '1'


# На случай если есть прокси ======
import httplib2
pi = httplib2.proxy_info_from_environment()
if pi:
    import socks
    socks.setdefaultproxy(pi.proxy_type, pi.proxy_host, pi.proxy_port)
    socks.wrapmodule(httplib2)

httplib2.Http()
#====================================

Builder.load_string(f"""
{open('kv/login.kv',            'r',  encoding='utf-8').read()}
{open('kv/mainscreen.kv',       'r',  encoding='utf-8').read()}
{open('kv/users.kv',            'r',  encoding='utf-8').read()}
{open('kv/new_user.kv',         'r',  encoding='utf-8').read()}
{open('kv/view_user.kv',        'r',  encoding='utf-8').read()}
{open('kv/new_project.kv',      'r',  encoding='utf-8').read()}
{open('kv/project.kv',          'r',  encoding='utf-8').read()}
{open('kv/project_team.kv',     'r',  encoding='utf-8').read()}
{open('kv/add_team_user.kv',    'r',  encoding='utf-8').read()}
{open('kv/remove_team_user.kv', 'r',  encoding='utf-8').read()}
{open('kv/create_reference.kv', 'r',  encoding='utf-8').read()}
""")


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
        return sm
    
    
if __name__ == '__main__':
    app = Gazel_cl()
    app.run()
