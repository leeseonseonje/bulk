import time
from concurrent.futures import ThreadPoolExecutor

from src.main.app.bulk.db_data_type import *
from src.main.app.init.db_connection import get_connection


def bulk_insert_mysql(table, row, is_random):
    conn = get_connection()
    start = time.time()
    divide = 10000
    if row > divide:
        loop = row / divide
        remaining = row % divide

        executor = ThreadPoolExecutor(10)
        for i in range(int(loop)):
            executor.submit(bulk_insert_execute, table, divide, is_random)
        if remaining:
            bulk_insert_execute(table, remaining, is_random)
        executor.shutdown(wait=True)

    else:
        bulk_insert_execute(table, row, is_random)
    end = time.time() - start
    print(f'working time: {datetime.timedelta(seconds=end)}')


def bulk_insert_execute(table, row, is_random):
    conn = get_connection()

    cursor = conn.cursor()

    try:
        query = []
        data = []
        record = []
        columns = declare_insert_query(cursor, query, table)

        for i in range(row):
            for column in columns:
                data_type = column[1]
                if is_not_auto_increment(column[5]):
                    column_value = DataType.type_checking_and_value_generate(data_type, is_random)
                    data.append(f"'{column_value}'")

            query_assembly(data, record)
        query.append(f'{", ".join(record)}')
        count = cursor.execute(''.join(query))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        conn.close()


def declare_insert_query(cursor, query, table):
    columns = []
    query.append(f'insert into {table} (')
    cursor.execute('desc ' + table)
    columns_info = cursor.fetchall()
    for column in columns_info:
        if is_not_auto_increment(column[5]):
            columns.append(column[0])
    query.append(f'{", ".join(columns)}) values ')
    return columns_info


def is_not_auto_increment(column):
    if not column:
        return True
    else:
        return False


def query_assembly(data, record):
    record.append(f'({", ".join(data)})')
    data.clear()
