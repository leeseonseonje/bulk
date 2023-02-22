from src.main.app.init.db_connection import get_connection


def delete_table(table: str):
    conn = get_connection()

    cursor = conn.cursor()

    try:
        count = cursor.execute('delete from ' + table)

        conn.commit()
        print(f'delete rows: {count}')
    except:
        conn.rollback()
        print('rollback')
