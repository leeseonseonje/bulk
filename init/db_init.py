import typer
import pymysql
import psycopg2

from src.main.app.util.typer_prompt import *
from src.main.app.repository.pickle_db_info_repository import save_db_info


class InitDB:

    def __init__(self, name):
        self.name = name

    def mysql(self):
        while True:
            host, port, user, password, db = host_port_user_password_db()
            isCorrect = entered_db_information(host, port, user, password, db)
            if isCorrect:
                try:
                    conn = pymysql.connect(host=host, port=int(port), user=user, password=password, db=db, charset='utf8')
                    success_connect(self.name, host, port, user, password, db, conn)
                except:
                    typer.echo('connect failed!!')

                break

    def postgres(self):
        while True:
            host, port, user, password, db = host_port_user_password_db()
            isCorrect = entered_db_information(host, port, user, password, db)
            if isCorrect:
                try:
                    conn = psycopg2.connect(host=host, port=int(port), user=user, password=password, dbname=db)
                    success_connect(self.name, host, port, user, password, db, conn)
                except:
                    typer.echo('connect failed!!')
                break


def success_connect(db_name, host, port, user, password, db, conn):
    conn.close()
    save_db_info(db_name, host, port, user, password, db)
    typer.echo('connect success!!')
