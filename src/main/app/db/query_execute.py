from src.main.app.init.db_connection import get_connection


def __sql__(query: str):
    conn = get_connection()

    cursor = conn.cursor()

    try:
        count = cursor.execute(query)
        conn.commit()
        records = cursor.fetchall()
        print(f'{count}')
        if records:
            print(f'{records}')
    except:
        conn.rollback()
        print('rollback')
