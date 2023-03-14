import datetime
import time

from src.main.app.init.db_connection import get_connection
from concurrent.futures import ThreadPoolExecutor


def delete_table(table):
    start = time.time()

    pk_column_name, pk = get_first_pk(table)

    limit = 10000
    index = -(limit - 1)

    executor = ThreadPoolExecutor(10)
    for _ in range(100):
        index += limit
        executor.submit(delete, table, index, limit, pk_column_name, pk)

    executor.shutdown(wait=True)
    end = time.time() - start
    print(f'working time: {datetime.timedelta(seconds=end)}')


def get_first_pk(table):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(f'select * from {table} limit {1}')
        row = cursor.fetchone()
        pk_column_name = cursor.description[0][0]
        pk = row[0]
        return pk_column_name, pk

    except Exception as e:
        print(e)

    finally:
        conn.close()


def delete(table, index, limit, pk_column_name, pk):
    conn = get_connection()

    cursor = conn.cursor()

    try:
        next_pk = pk + (index - 1)
        limit += next_pk
        cursor.execute(f'delete from {table} where {pk_column_name} between {next_pk} and {limit}')

        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        conn.close()
