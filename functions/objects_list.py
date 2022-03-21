import requests, os 

from config import DATABASE_URL

from value import HEADERS, VIEW_PROJECT, VIEW_REFERENCE, \
                  File, FILES_LIST
from config import ROOT, get_hash_md5


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

    def find_file(NAME):
        for file in FILES_CLIENT:
            if file.name == NAME:
                FILES_CLIENT.drop(file)
                return True
        return False

    if req.json() is None and len(FILES_CLIENT) == 0 :
        FILES_LIST.clear()
        f = File()
        f.name = ''
        f.type = 'Файлов нет'
        f.color = 'grey'
        FILES_LIST.append(f)
    elif req.json() is None and len(FILES_CLIENT) != 0:
        FILES_LIST.clear()
        for file in FILES_CLIENT:
            f = File()
            f.name = file.name
            f.path = file
            f.type = 'Не загружен в базу'
            f.color = 'red'
            FILES_LIST.append(f) 
    
    elif not req.json() is None and len(FILES_CLIENT) == 0 :
        FILES_LIST.clear()
        for file in list(req.json()):
            f = File()
            f.id = file['o_id']
            f.name = file['o_file_name']
            f.path = ''
            f.type = 'Готов к загрузке'
            f.color = 'green'
            FILES_LIST.append(f)

    elif not req.json() is None and len(FILES_CLIENT) != 0 :
        FILES_LIST.clear()
        for file in list(req.json()):
            if find_file(file['o_file_name']):
                "если файл из базы найден на клиенте"
                if file['o_hash_sum'] == get_hash_md5(PATH / file['o_file_name']):
                    f = File()
                    f.id = file['o_id']
                    f.name = file['o_file_name']
                    f.path = PATH / file['o_file_name']
                    f.type = 'не требует синхронизации'
                    f.color = 'Purple'
                    FILES_LIST.append(f)
                else:
                    f = File()
                    f.id = file['o_id']
                    f.name = file['o_file_name']
                    f.path = PATH / file['o_file_name']
                    f.type = 'Готов к обновлению'
                    f.color = 'Orange'
                    FILES_LIST.append(f)
            else:
                "если не найден"
                f = File()
                f.id = file['o_id']
                f.name = file['o_file_name']
                f.path = PATH / file['o_file_name']
                f.type = 'Готов к загрузке'
                f.color = 'green'
                FILES_LIST.append(f)

        for file in FILES_CLIENT:
            f = File()
            f.id = ''
            f.name = file.name
            f.path = file
            f.type = 'Не загружен в базу'
            f.color = 'red'
            FILES_LIST.append(f)
    
    #if not "error" in req.text:
    #    return req.json()
    #else:
    #    return []
