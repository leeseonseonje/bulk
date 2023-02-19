from src.main.app.init.db_connection import get_connection

from src.main.app.util.random.random_generator import *


def bulk_insert(table: str, row: int):
    conn = get_connection()

    cursor = conn.cursor()

    try:
        query = []
        columns = []
        data = []
        datas = []
        query.append(f'insert into {table} (')
        count = cursor.execute('desc ' + table)
        records = cursor.fetchall()
        for record in records:
            if not record[5]:
                columns.append(record[0])
        query.append(f'{", ".join(columns)}) values ')
        for i in range(row):
            for record in records:
                n = i + 1
                if not record[5]:
                    if record[1] == 'int' or record[1] == 'bigint':
                        r = random_integer(n)
                        data.append(str(r))
                    if record[1] == 'varchar(256)':
                        r = random_string(256, n)
                        data.append(f"'{str(r)}'")
                    if record[1] == 'date':
                        r = random_date()
                        data.append(f"'{str(r)}'")
            datas.append(f'({", ".join(data)})')
            data.clear()
        query.append(f'{", ".join(datas)}')
        count = cursor.execute(''.join(query))
        conn.commit()
        print(f'insert rows: {count}')
    except:
        conn.rollback()
        print('rollback')
