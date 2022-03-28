import requests, os, base64

from config import DATABASE_URL

from value import HEADERS, VIEW_REFERENCE, FILES_LIST


def objects_load(INDEX):

    url = DATABASE_URL + 'download_object'

    value = dict(
            R_ID = str(VIEW_REFERENCE.r_id),
            O_ID = FILES_LIST[INDEX].id
            )
    try:
        with requests.get(url, headers=HEADERS, json=value, stream=True) as req:
            with open(FILES_LIST[INDEX].path, 'wb') as file:
                for chunk in req.iter_content(chunk_size=8192): 
                    file.write(chunk)
    except:
        if 'error' in req.text:
            return req.json()
    else:
        return {'message' : 'Файл успешно загружен'}
