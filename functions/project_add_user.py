import requests

from config import DATABASE_URL

from value import HEADERS, USER


def project_add_user(project : str, username : str, access: int) -> str:
    url = DATABASE_URL + 'add_user_to_team'
    values = dict(
            author = USER.username,
            p_name = project,
            username = username,
            access_level = access
            )
    
    req = requests.post(url, headers=HEADERS, json=values )

    if not "error" in req.text:
        return req.json()["message"]
    else:
        return req.json()["error"]

