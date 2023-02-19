import datetime

from src.main.app.init.db_connection import get_connection
import random

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
                if not record[5]:
                    if record[1] == 'int' or record[1] == 'bigint':
                        r = random.randrange(1, 1000)
                        data.append(str(r))
                    if record[1] == 'varchar(256)':
                        r = random.randrange(1, 1000)
                        data.append(str(r))
                    if record[1] == 'date':
                        now = datetime.datetime.now()
                        data.append(f"'{str(now)}'")
            datas.append(f'({", ".join(data)})')
            data.clear()
        query.append(f'{", ".join(datas)}')
        count = cursor.execute(''.join(query))
        conn.commit()
        print(count)
    except:
        conn.rollback()
        print('rollback')