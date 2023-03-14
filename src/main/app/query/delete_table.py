import datetime
import time

from src.main.app.init.db_connection import get_connection
from concurrent.futures import ThreadPoolExecutor


def delete_table(table):
    start = time.time()
    executor = ThreadPoolExecutor(10)
    while True:
        future = executor.submit(delete, table)
        if future.result() == 0:
            break
    end = time.time() - start
    print(f'working time: {datetime.timedelta(seconds=end)}')


def delete(table):
    conn = get_connection()

    cursor = conn.cursor()

    try:
        limit = 100000
        count = cursor.execute(f'delete from {table} limit {limit}')

        conn.commit()
        return count
    except:
        conn.rollback()
        print('rollback')
