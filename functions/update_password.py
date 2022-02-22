import requests

from config import DATABASE_URL, SALT

from value import USER, VIEW_USER

from passlib.hash import md5_crypt

def hash_password(password: str) -> str:
    "Хеширование пароля"
    return md5_crypt.encrypt(password,salt=SALT)


def update_password(password : str):
    url = DATABASE_URL + 'update_password'
    
    json = {
            "token" : USER.token,
            "username" : VIEW_USER.username,
            "password_hash" : hash_password(password) 
            }
    req = requests.put(url, json = json)

    if "error" in req.text:
        return req.json()["error"]
    else:
        return req.json()["message"]
 
