import requests

from config import DATABASE_URL

from value import VIEW_PROJECT, HEADERS

def project_info(name : str):
    url = DATABASE_URL + 'project_info'
    
    req = requests.get(url, headers = HEADERS, json = {"p_name" : name })
    
    if not "error" in req.text:
        res = req.json()
        VIEW_PROJECT.p_name = res["p_name"]
        VIEW_PROJECT.p_description = res["p_description"]


