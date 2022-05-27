import requests


def check_server_status(ip: str):
    try:
        if requests.get(ip).status_code == 200:
            return True
    except Exception:
        return False
