import requests

from config import DATABASE_URL

from value import HEADERS, USER, VIEW_PROJECT

def project_remove_user(project : str, username : str) -> str:
    url = DATABASE_URL + 'remove_user_from_team'
    values = dict(
            p_name = project,
            username = username
            )
    
    req = requests.delete(url, headers=HEADERS, json=values )

    if "message" in req.text:
        url = DATABASE_URL + 'create_log'
        value = dict(
                P_ID = VIEW_PROJECT.p_id,
                EVENT = f"Удалён из команды {project} пользователь {username}"
                )
        r = requests.post(url, headers=HEADERS, json=value)
       
        return req.json()["message"]
    elif "error" in req.text:
        return req.json()["error"]

