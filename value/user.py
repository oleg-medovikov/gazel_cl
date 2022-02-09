from kivy.properties import StringProperty, BooleanProperty
from uuid import UUID

class User():
    first_name : StringProperty('')
    secon_name : StringProperty('')
    username : StringProperty('')
    password_hash : StringProperty('')
    position : StringProperty('')
    token    : StringProperty('')
    admin    : BooleanProperty('')

 
USER = User()
