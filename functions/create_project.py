import requests

from config import DATABASE_URL
from value import USER, Project


def create_project(new_project : Project):

    url = DATABASE_URL + 'create_project'

    values = {"p_name" : new_project.p_name,
              "p_description" : new_project.p_description
            }
    req = requests.post(url, headers = {"token" : USER.token} , json = values)

    #print(values)
    #print(req.text)
    
    if "error" in req.text:
        return  req.json()["error"]
    else:
        return  req.json()["message"]
