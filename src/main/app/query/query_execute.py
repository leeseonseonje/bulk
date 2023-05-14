from src.main.app.init.db_connection import get_connection


def __sql__(query: str):
    conn = get_connection()

    cursor = conn.cursor()

    try:
        count = cursor.execute(query)
        conn.commit()
        records = cursor.fetchall()
        print(f'count: {count}')
        if records:
            for r in records:
                print(f'{r}')
    except:
        conn.rollback()
        print('rollback')
    finally:
        conn.close()
