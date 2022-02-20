import requests

from config import DATABASE_URL
from value import USER, Project


def create_project(new_project : Project):

    url = DATABASE_URL + 'create_project'

    values = new_project.__dict__
    req = requests.post(url, json = values)

    #print(values)
    #print(req.text)
    
    if "error" in req.text:
        return  req.json()["error"]
    else:
        return  req.json()["message"]
