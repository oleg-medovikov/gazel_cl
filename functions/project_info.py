import requests

from config import DATABASE_URL

from value import USER, VIEW_PROJECT

def project_info(name : str):
    url = DATABASE_URL + 'project_info'
    
    json = {
            "token" : USER.token,
            "p_name" : name
            }
    req = requests.post(url, json = json)
    
    if not "error" in req.text:
        res = req.json()
        VIEW_PROJECT.p_name = res["p_name"]
        VIEW_PROJECT.p_description = res["p_description"]


