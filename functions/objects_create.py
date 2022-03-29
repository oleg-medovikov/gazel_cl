import requests, os 

from config import DATABASE_URL

from value import HEADERS, VIEW_PROJECT, VIEW_REFERENCE, \
                  File, FILES_LIST

from config import ROOT, get_hash_md5

def objects_create(INDEX):

    url = DATABASE_URL + 'create_object'
    value = dict(
            R_ID = str(VIEW_REFERENCE.r_id),
            O_HASH_SUM = get_hash_md5( FILES_LIST[INDEX].path ), 
            FILE_NAME  = FILES_LIST[INDEX].name
            )

    file = {'file': open(FILES_LIST[INDEX].path,'rb')}

    req = requests.post(url, headers=HEADERS, data=value, files=file)
    
    
    if "message" in req.text:
        url = DATABASE_URL + 'create_log'
        value = dict(
                P_ID = VIEW_PROJECT.p_id,
                R_ID = VIEW_REFERENCE.r_id,
                EVENT = f"Загружен в базу {FILES_LIST[INDEX].name}"
                )
        r = requests.post(url, headers=HEADERS, json=value)

    return req.json()
