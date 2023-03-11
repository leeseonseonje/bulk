from src.main.app.init.db_connection import get_connection
from concurrent.futures import ThreadPoolExecutor


def delete_table(table: str):
    conn = get_connection()

    cursor = conn.cursor()

    try:
        executor = ThreadPoolExecutor(10)
        count = cursor.execute('delete from ' + table)

        conn.commit()
        print(f'delete rows: {count}')
    except:
        conn.rollback()
        print('rollback')
