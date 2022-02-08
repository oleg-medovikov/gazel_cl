from passlib.hash import md5_crypt
import requests

from config import DATABASE_URL, SALT, USER_FIRST_NAME, USER_TOKEN, USER_POSITION

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

    #print("server: ", url)
    #print("send json: ", values)
    #print("server answer: ", req.text)
    
    if  "error" in req.text:
        return  False, req.json()["error"]
    if req.json()["message"] == "Вы успешно вошли в систему":
        USER_FIRST_NAME = req.json()["first_name"]
        USER_POSITION = req.json()["position"]
        USER_TOKEN = req.json()["token"]
        return True, req.json()
