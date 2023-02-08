import requests
import custom_exceptions

URL = "https://fakestoreapi.com/"


def create(path, data_to_add, logger=None):
    logger.debug(f"Creating {path}...")
    result = requests.post(f"{URL}{path}", data=data_to_add)
    logger.debug(f"{path} Created [{result}]")


def read(path, logger=None):
    logger.debug(f"Starting collect data from {URL}")
    data = None
    try:
        data = requests.get(f"{URL}{path}")
        logger.debug(f"Data [{data}] collected from {URL}")
    except requests.exceptions.ConnectionError as cerr:
        logger.error(cerr)
        raise custom_exceptions.InvalidURlException(
            f"An invalid URL was provided: [{URL}]"
        )
    except Exception as err:
        print(f"Something when wrong: [{type(err)}]")
    logger.debug(f"Ended collection data...")
    return data
