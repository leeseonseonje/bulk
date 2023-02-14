from src.repository.pickle_db_info_repository import db_info_load
import pymysql


def execute():
    host, port, user, password, db = db_info_load()
    con = pymysql.connect(host=host, port=int(port), user=user, password=password, db=db, charset='utf8')

    cursor = con.cursor()
    query = "insert into test (col1, col2) values (1, 'python_test'), (2, 'test');"
    count = cursor.execute(query)
    print(f"{count} rows insert")
    con.commit()
    con.close()