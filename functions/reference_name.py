import requests

from config import DATABASE_URL
from value import   HEADERS, VIEW_PROJECT, VIEW_REFERENCE


def reference_name():

    url = DATABASE_URL + 'reference_name'
    value = dict(
            P_NAME = VIEW_PROJECT.p_name,
            R_CODE_NAME_LEVEL_1 = VIEW_REFERENCE.r_level1,
            R_CODE_NAME_LEVEL_2 = int(VIEW_REFERENCE.r_level2),
            R_CODE_NAME_LEVEL_3 = int(VIEW_REFERENCE.r_level3)
            )

    req = requests.get(url, headers = HEADERS , json = value )
    
    if not "error" in req.text:
        VIEW_REFERENCE.r_id = req.json()["r_id"]
        VIEW_REFERENCE.r_name = req.json()["r_name"]

