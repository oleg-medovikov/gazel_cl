from kivy.properties import StringProperty, BooleanProperty

class User():
    first_name  : StringProperty('')
    second_name : StringProperty('')
    token       : StringProperty('')
    position    : StringProperty('')
    admin       : BooleanProperty(False)


USER = User()
