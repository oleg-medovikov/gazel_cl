import requests

from config import DATABASE_URL

from value import HEADERS, VIEW_LOGS, VIEW_LOGS_DATES, Log


def logs_list(ID) -> list:
    url = DATABASE_URL + 'list_log'

    req = requests.get(url, headers=HEADERS, json=ID)
    

    if "error" in req.text:
        return []
    else:
        VIEW_LOGS.clear()
        VIEW_LOGS_DATES.clear()

        for log in req.json():
            if not log["date"] in VIEW_LOGS_DATES:
                VIEW_LOGS_DATES.append(log["date"])
            
            LOG = Log()
            LOG.p_name   = log["p_name"]
            LOG.r_name   = log["r_name"]
            LOG.r_code   = log["r_code"]
            LOG.username = log["username"]
            LOG.user     = log["user"]
            LOG.date     = log["date"]
            LOG.time     = log["time"]
            LOG.event    = log["event"]
            
            VIEW_LOGS.append(LOG)
