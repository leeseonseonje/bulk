import datetime
import time

from concurrent.futures import ThreadPoolExecutor

from src.app.init.db_connection import get_connection


def delete_table(table):
    start = time.time()

    pk_column_name, pk = get_first_pk(table)

    limit = 10000
    index = -(limit - 1)

    executor = ThreadPoolExecutor(10)
    loop = 0
    while True:
        index += limit
        loop += 1

        if loop % 10 == 0:
            delete_count = executor.submit(delete, table, index, limit, pk_column_name, pk)

            if delete_count.result() == 0:
                break

        else:
            executor.submit(delete, table, index, limit, pk_column_name, pk)

    executor.shutdown(wait=True)
    end = time.time() - start
    print(f'delete time: {datetime.timedelta(seconds=end)}')


def get_first_pk(table):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(f'select * from {table} limit {1}')
        row = cursor.fetchone()
        print(row)
        pk_column_name = cursor.description
        print(pk_column_name)
        pk = row[0]
        print(pk)
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
        print(next_pk)
        limit += next_pk

        count = cursor.execute(f'delete from {table} where {pk_column_name} between {next_pk} and {limit}')
        conn.commit()

        return count

    except Exception as e:
        conn.rollback()
        print(e)

    finally:
        conn.close()
