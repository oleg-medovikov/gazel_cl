from passlib.hash import md5_crypt
import requests

from config import DATABASE_URL, SALT
from user import USER

def hash_password(password: str) -> str:
    "Хеширование пароля"
    return md5_crypt.encrypt(password,salt=SALT)

def login(username:str, password:str):
    url = DATABASE_URL + 'login'
    values = {
        "username" : username,
        "password_hash" : hash_password(password) 
            }
    req = requests.post(url, json = values)

    if  "error" in req.text:
        return  False, req.json()["error"]
    if req.json()["message"] == "Вы успешно вошли в систему":
        USER.first_name  = req.json()["first_name"]
        USER.second_name = req.json()["second_name"]
        USER.position    = req.json()["position"]
        USER.token       = req.json()["token"]
        USER.admin       = req.json()["admin"]
        return True, req.json()
