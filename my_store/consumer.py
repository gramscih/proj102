import requests
import custom_exceptions
import logging

URL = "https://akestoreapi.com/"

logging.basicConfig(level=logging.WARNING)


def create(path, data):
    pass


def read(path):
    logging.debug(f"Starting collect data from {URL}")
    data = None
    try:
        data = requests.get(f"{URL}{path}")
        logging.debug(f"Data [{data}] collected from {URL}")
    except requests.exceptions.ConnectionError as cerr:
        logging.error(cerr)
        raise custom_exceptions.InvalidURlException(
            f"An invalid URL was provided: [{URL}]"
        )
    except Exception as err:
        print(f"Something when wrong: [{type(err)}]")
    logging.debug(f"Ended collection data...")
    return data
