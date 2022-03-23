import requests, os, base64

from config import DATABASE_URL

from value import HEADERS, VIEW_REFERENCE, FILES_LIST


def objects_load(INDEX):

    url = DATABASE_URL + 'download_object'

    value = dict(
            R_ID = str(VIEW_REFERENCE.r_id),
            O_ID = FILES_LIST[INDEX].id
            )

    req = requests.get(url, headers=HEADERS, json=value)

    if 'error' in req.text:
        return req.json()
    
    string = req.json()['o_binary'].encode('utf-8')

    with open( FILES_LIST[INDEX].path, "wb") as file:
        file.write(base64.decodebytes( string ) )

    return {'message' : 'Файл успешно загружен'}
