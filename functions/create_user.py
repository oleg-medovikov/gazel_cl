from passlib.hash import md5_crypt
import requests 

from config import DATABASE_URL, SALT
from value import HEADERS, USER

def hash_password(password: str) -> str:
    "Хеширование пароля"
    return md5_crypt.encrypt(password,salt=SALT)


def create_user(FIRST_NAME,SECOND_NAME,USERNAME,PASSWORD,POSITION,ADMIN):

    url = DATABASE_URL + 'new_user'
    
    PASSWORD_HASH = hash_password(PASSWORD)

    values = dict(
        first_name = FIRST_NAME,
        second_name = SECOND_NAME,
        username = USERNAME,
        password_hash = PASSWORD_HASH,
        position = POSITION,
        admin = ADMIN
        )

    req = requests.post(url, headers=HEADERS, json = values)
    
    if "error" in req.text:
        return False, req.json()["error"]
    else:
        return True, req.json()["message"]
