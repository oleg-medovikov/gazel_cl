import requests

from config import DATABASE_URL

from value import USER


def project_team_users(project: str) -> list:
    url = DATABASE_URL + 'list_team_users'

    req = requests.post(url, 
            json= {"token": USER.token,
                   "p_name" : project
                    })
    if not "error" in req.text:
        list_=[]
        for row in req.json():
            list_.append(row)

        list_.sort()
        return list_
