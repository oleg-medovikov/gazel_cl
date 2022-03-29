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

        url = DATABASE_URL + 'create_log'
        value = dict(
                P_ID = VIEW_PROJECT.p_id,
                R_ID = VIEW_REFERENCE.r_id,
                EVENT = f"Загружен локально {FILES_LIST[INDEX].name}"
                )
        r = requests.post(url, headers=HEADERS, json=value)


        return {'message' : 'Файл успешно загружен'}
