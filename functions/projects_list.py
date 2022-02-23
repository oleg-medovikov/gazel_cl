import requests

from config import DATABASE_URL

from value import HEADERS


def projects_list() -> list:
    url = DATABASE_URL + 'allow_projects'

    req = requests.get(url, headers=HEADERS)
    
    if not "error" in req.text:
        return req.json()
    else:
        return []
