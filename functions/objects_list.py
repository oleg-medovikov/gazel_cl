import requests, os, hashlib

from config import DATABASE_URL

from value import HEADERS, VIEW_PROJECT, VIEW_REFERENCE, \
                  File, FILES_LIST
from config import ROOT 


def get_hash_md5(filename):
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

def objects_list():
    
    CATALOG = VIEW_REFERENCE.r_level1 +'_' \
              + str(VIEW_REFERENCE.r_level2) + '_'  \
              + str(VIEW_REFERENCE.r_level3)

    PATH = ROOT / VIEW_PROJECT.p_name / CATALOG

    url = DATABASE_URL + 'objects_list'
    req = requests.get(url, headers=HEADERS, json=VIEW_REFERENCE.r_id)

    if not PATH.is_dir():
        os.makedirs(PATH)
        FILES_CLIENT = []    
    else:
        FILES_CLIENT = list(PATH.glob('*.*'))

    if req.json() is None and len(FILES_CLIENT) == 0 :
        FILES_LIST.clear()
        f = File()
        f.name = 'Файлов нет'
        f.color = 'grey'
        FILES_LIST.append(f)
    elif req.json() is None and len(FILES_CLIENT) != 0:
        FILES_LIST.clear()
        for file in FILES_CLIENT:
            f = File()
            f.name = file.name
            f.path = file
            f.color = 'red'
            FILES_LIST.append(f) 


    
    #if not "error" in req.text:
    #    return req.json()
    #else:
    #    return []
