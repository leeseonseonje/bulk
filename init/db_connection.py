import pymysql
import psycopg2

from src.main.app.repository.pickle_db_info_repository import load_db_info


class ConnectDB:

    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    def mysql(self):
        return pymysql.connect(host=self.host,
                               port=int(self.port),
                               user=self.user,
                               password=self.password,
                               db=self.db,
                               charset='utf8')

    def postgres(self):
        return psycopg2.connect(host=self.host,
                                port=int(self.port),
                                user=self.user,
                                password=self.password,
                                dbname=self.db)


def get_connection():
    db_name, host, port, user, password, db = load_db_info()
    connect_db = ConnectDB(host, port, user, password, db)
    return getattr(connect_db, db_name)()
