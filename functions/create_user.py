from passlib.hash import md5_crypt
import requests 

from config import DATABASE_URL, SALT
from value import User, USER

def hash_password(password: str) -> str:
    "Хеширование пароля"
    return md5_crypt.encrypt(password,salt=SALT)


def create_user(new_user: User):
    new_user.token = USER.token
    new_user.password_hash = hash_password(new_user.password_hash)

    url = DATABASE_URL + 'new_user'
    values = new_user.__dict__
    req = requests.post(url, json = values)

    #print(values)
    #print(req.text)
    
    if "error" in req.text:
        return False, req.json()["error"]
    else:
        return True, req.json()["message"]
