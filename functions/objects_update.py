import requests, os 

from config import DATABASE_URL

from value import HEADERS, VIEW_PROJECT, VIEW_REFERENCE, \
                  File, FILES_LIST

from config import ROOT, get_hash_md5

def objects_update(INDEX):

    url = DATABASE_URL + 'update_object'
    value = dict(
            R_ID = str(VIEW_REFERENCE.r_id),
            O_HASH_SUM = get_hash_md5( FILES_LIST[INDEX].path ), 
            O_ID  = FILES_LIST[INDEX].id
            )

    file = {'file': open(FILES_LIST[INDEX].path,'rb')}

    req = requests.put(url, headers=HEADERS, data=value, files=file)
    if "message" in req.text:
        url = DATABASE_URL + 'create_log'
        value = dict(
                P_ID = VIEW_PROJECT.p_id,
                R_ID = VIEW_REFERENCE.r_id,
                EVENT = f"Обновлён файл {FILES_LIST[INDEX].name}"
                )
        r = requests.post(url, headers=HEADERS, json=value)
    
    return req.json()
