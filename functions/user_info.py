import requests

from config import DATABASE_URL

from value import USER, VIEW_USER

def user_info(username : str):
    url = DATABASE_URL + 'user_info'
    
    json = {
            "token" : USER.token,
            "username" : username
            }
    req = requests.get(url, headers = json)
    
    if not "error" in req.text:
        res = req.json()
        VIEW_USER.first_name = res["first_name"]
        VIEW_USER.second_name = res["second_name"]
        VIEW_USER.username = res["username"]
        VIEW_USER.position = res["position"]
        VIEW_USER.admin = res["admin"]


