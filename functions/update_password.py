import requests

from config import DATABASE_URL, SALT

from value import HEADERS, VIEW_USER

from passlib.hash import md5_crypt

def hash_password(password: str) -> str:
    "Хеширование пароля"
    return md5_crypt.encrypt(password,salt=SALT)


def update_password(password : str):
    url = DATABASE_URL + 'update_password'
    
    value = dict(
            username = VIEW_USER.username,
            password_hash = hash_password(password) 
            )
    req = requests.put(url, headers=HEADERS,  json = value)

    if "error" in req.text:
        return req.json()["error"]
    else:
        return req.json()["message"]
 
