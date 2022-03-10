import requests

from config import DATABASE_URL
from value import   HEADERS, VIEW_PROJECT, VIEW_REFERENCE


def reference_level2():

    url = DATABASE_URL + 'reference_level2'
    value = dict(
            P_NAME = VIEW_PROJECT.p_name,
            R_CODE_NAME_LEVEL_1 = VIEW_REFERENCE.r_level1
            )

    req = requests.post(url, headers = HEADERS , json = value )

    if "error" in req.text:
        return  req.json()["error"]
    else:
        return  req.json()
