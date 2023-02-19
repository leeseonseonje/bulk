from src.main.app.db.db_data_type import *
from src.main.app.init.db_connection import get_connection


def bulk_insert_mysql(table: str, row: int):
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
                if is_not_primary_key(column[5]):
                    type_checking_and_value_generate(data, data_type, i + 1)

            query_assembly(data, record)
        query.append(f'{", ".join(record)}')
        count = cursor.execute(''.join(query))
        conn.commit()
        print(f'insert rows: {count}')
    except:
        conn.rollback()
        print('rollback')


def declare_insert_query(cursor, query, table):
    columns = []
    query.append(f'insert into {table} (')
    cursor.execute('desc ' + table)
    columns_info = cursor.fetchall()
    for column in columns_info:
        if is_not_primary_key(column[5]):
            columns.append(column[0])
    query.append(f'{", ".join(columns)}) values ')
    return columns_info


def is_not_primary_key(column):
    if not column:
        return True
    else:
        return False


def query_assembly(data, record):
    record.append(f'({", ".join(data)})')
    data.clear()
