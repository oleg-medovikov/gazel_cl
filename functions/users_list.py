import requests

from config import DATABASE_URL

from value import HEADERS


def users_list() -> list:
    url = DATABASE_URL + 'users_list'

    req = requests.get(url, headers = HEADERS )

    if not "error" in req.text:
        list_ = []
        for row in req.json():
            list_.append(row['username'])
        
        list_.sort()
        return list_
