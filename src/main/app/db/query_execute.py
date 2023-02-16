import pymysql as pymysql

from src.main.app.init.db_connection import get_connection


def execute(query: str):
    con = get_connection()

    cursor = con.cursor()

    try:
        result = cursor.execute(query)
        con.commit()
        print(f'{cursor.fetchall()}')
    except:
        con.rollback()
        print('rollback')
