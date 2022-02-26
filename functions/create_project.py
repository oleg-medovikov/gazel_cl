import requests

from config import DATABASE_URL
from value import   HEADERS


def create_project(P_NAME : str,P_DESCRIPTION : str):

    url = DATABASE_URL + 'create_project'

    values = {"p_name" : P_NAME,
              "p_description" : P_DESCRIPTION
            }
    req = requests.post(url, headers = HEADERS , json = values)
    
    print(req.text)

    if "error" in req.text:
        return  req.json()["error"]
    else:
        return  req.json()["message"]
