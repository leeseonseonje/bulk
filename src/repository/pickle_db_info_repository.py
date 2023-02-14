import pickle


def db_info_save(host: str, port: int, user: str, password: str, db: str):
    with open('./resource/db.pickle', 'wb') as save:
        pickle.dump([host, port, user, password, db], save)


def db_info_load():
    with open('./resource/db.pickle', 'rb') as load:
        return pickle.load(load)
