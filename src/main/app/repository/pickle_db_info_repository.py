import pickle
from pathlib import Path

path = str(Path(__file__).parent.parent.parent) + '/resource/db.pickle'


def save_db_info(db_connection):
    with open(path, 'wb') as save:
        pickle.dump([db_connection], save)


def load_db_info():
    with open(path, 'rb') as load:
        return pickle.load(load)[0]

