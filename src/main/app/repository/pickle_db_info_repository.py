import pickle
from pathlib import Path

path = str(Path(__file__).parent.parent.parent) + '/resource/db.pickle'


def save_db_info(db_name: str, host: str, port: int, user: str, password: str, db: str):
    with open(path, 'wb') as save:
        pickle.dump([db_name, host, port, user, password, db], save)


def load_db_info():
    with open(path, 'rb') as load:
        return pickle.load(load)


def load_db_name():
    with open(path, 'rb') as load:
        return pickle.load(load)[0]
