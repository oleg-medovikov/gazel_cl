import requests

from config import DATABASE_URL

from value import HEADERS, USER, VIEW_PROJECT


def project_add_user(project : str, username : str, access: int) -> str:
    url = DATABASE_URL + 'add_user_to_team'
    values = dict(
            author = USER.username,
            p_name = project,
            username = username,
            access_level = access
            )
    
    req = requests.post(url, headers=HEADERS, json=values )

    if "message" in req.text:
        url = DATABASE_URL + 'create_log'
        value = dict(
                P_ID = VIEW_PROJECT.p_id,
                EVENT = f"Добавлен в команду {project} пользователь {username} с уровнем прав {access}"
                )
        r = requests.post(url, headers=HEADERS, json=value)

        return req.json()["message"]

    elif "error" in req.text:
        return req.json()["error"]

