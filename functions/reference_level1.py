import requests

from config import DATABASE_URL
from value import   HEADERS, VIEW_PROJECT


def reference_level1():

    url = DATABASE_URL + 'reference_level1'

    req = requests.post(url, headers = HEADERS , json = VIEW_PROJECT.p_name)

    if "error" in req.text:
        return  req.json()["error"]
    else:
        return  req.json()
