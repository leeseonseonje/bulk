from src.repository.pickle_db_info_repository import load_db_info
import pymysql


def execute():
    con = load_connection()

    cursor = con.cursor()

    query = "insert into test (col1, col2) values (1, 'python_test'), (2, 'test');"
    count = cursor.execute(query)
    print(f"{count} rows insert")
    con.commit()

    query = "insert into test (col1, col2) values (1, 'python_test'), (2, 'test');"
    count = cursor.execute(query)
    print(f"{count} rows insert")
    con.commit()
