import requests

from config import DATABASE_URL
from value import   HEADERS, VIEW_PROJECT


def reference_create(
        NAME : str,
        LEVEL_1 : str,
        LEVEL_2 : str,
        LEVEL_3 : str
        ):

    url = DATABASE_URL + 'create_reference'

    values = dict(
            P_NAME =  VIEW_PROJECT.p_name,
            R_NAME = NAME,
            R_CODE_NAME_LEVEL_1 = LEVEL_1,
            R_CODE_NAME_LEVEL_2 = int(LEVEL_2),
            R_CODE_NAME_LEVEL_3 = int(LEVEL_3) 
            )

    req = requests.post(url, headers = HEADERS , json = values)

    if "error" in req.text:
        return  req.json()["error"]
    else:
        url = DATABASE_URL + 'create_log'
        value = dict(
                P_ID = VIEW_PROJECT.p_id,
                EVENT = f"Создано обозначение {LEVEL_1 +'_'+LEVEL_2 +'_'+ LEVEL_3}"
                )
        r = requests.post(url, headers=HEADERS, json=value)

        return  req.json()["message"]
