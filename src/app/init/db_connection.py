import sys

import pymysql
import psycopg2

from src.app.repository.pickle_db_info_repository import load_db_info
from src.app.init.db_connection_dto import DBConnectionDto


class DBConnection:

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
    try:
        db_info: DBConnectionDto = load_db_info()
        connect_db = DBConnection(db_info.host, db_info.port, db_info.user, db_info.password, db_info.db)
        return getattr(connect_db, db_info.dbms)()
    except:
        print('connect failed!!')
        sys.exit(1)
