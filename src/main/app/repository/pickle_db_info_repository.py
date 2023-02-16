import pickle


def save_db_info(db_name: str, host: str, port: int, user: str, password: str, db: str):
    with open('../../resource/db.pickle', 'wb') as save:
        pickle.dump([db_name, host, port, user, password, db], save)


def load_db_info():
    with open('../../resource/db.pickle', 'rb') as load:
        return pickle.load(load)
