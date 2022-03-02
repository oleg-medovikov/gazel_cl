from passlib.hash import md5_crypt
import requests

from config import DATABASE_URL, SALT
from value import USER, HEADERS

def hash_password(password: str) -> str:
    "Хеширование пароля"
    return md5_crypt.encrypt(password,salt=SALT)

def login(USERNAME:str, PASSWORD:str):
    url = DATABASE_URL + 'login'
    values = dict(
                username = USERNAME,
                password_hash = hash_password(PASSWORD) 
                )
    req = requests.get(url, json = values)

    if  "error" in req.text:
        return  False, req.json()["error"]
    if req.json()["message"] == "Вы успешно вошли в систему":
        USER.first_name  = req.json()["first_name"]
        USER.second_name = req.json()["second_name"]
        USER.position    = req.json()["position"]
        USER.username    = USERNAME
        USER.admin       = req.json()["admin"]
        
        HEADERS["Authorization"] = req.json()["token"]
        return True, req.json()
