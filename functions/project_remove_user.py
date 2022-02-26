import requests

from config import DATABASE_URL

from value import HEADERS, USER


def project_remove_user(project : str, username : str) -> str:
    url = DATABASE_URL + 'remove_user_from_team'
    values = dict(
            p_name = project,
            username = username
            )
    
    req = requests.delete(url, headers=HEADERS, json=values )

    if not "error" in req.text:
        return req.json()["message"]
    else:
        return req.json()["error"]

