import requests 

from config import DATABASE_URL

from value import HEADERS, VIEW_PROJECT, VIEW_REFERENCE, FILES_LIST

def objects_delete(o_id):
    
    for file in FILES_LIST:
        if file.id == o_id:
            FILENAME = file.name
            break

    url = DATABASE_URL + 'delete_object'
    value = dict(
            R_ID = str(VIEW_REFERENCE.r_id),
            O_ID  = o_id
            )

    req = requests.delete(url, headers=HEADERS, json=value)

    if "message" in req.text:
        url = DATABASE_URL + 'create_log'
        value = dict(
                P_ID = VIEW_PROJECT.p_id,
                R_ID = VIEW_REFERENCE.r_id,
                EVENT = f"Из базы удален файл {FILENAME}"
                )
        r = requests.post(url, headers=HEADERS, json=value)

    return req.json()
