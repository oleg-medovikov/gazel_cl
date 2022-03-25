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
    
    print(req.text)
    return req.json()
