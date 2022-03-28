import requests 

from config import DATABASE_URL

from value import HEADERS, VIEW_REFERENCE, FILES_LIST

def objects_delete(o_id):

    url = DATABASE_URL + 'delete_object'
    value = dict(
            R_ID = str(VIEW_REFERENCE.r_id),
            O_ID  = o_id
            )

    req = requests.delete(url, headers=HEADERS, json=value)

    return req.json()
