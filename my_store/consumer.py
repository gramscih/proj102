import requests

URL = "https://akestoreapi.com/"


def create(path, data):
    pass


def read(path):
    data = None
    try:
        data = requests.get(f"{URL}{path}")
    except:
        pass
        print("Something when wrong")
    return data
