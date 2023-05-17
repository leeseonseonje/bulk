from src.app.init.db_connection import get_connection
from src.app.util.typer_prompt import *
from src.app.repository.pickle_db_info_repository import save_db_info


def db_init(dbms):
    connection_dto = host_port_user_password_db(dbms)
    save_db_info(connection_dto)
    get_connection()
    print('connect success!!')
