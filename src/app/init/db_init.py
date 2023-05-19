import typer
from src.app.init.db_connection import get_connection
from src.app.init.db_connection_config import DBConnectionConfig
from src.app.repository.pickle_db_info_repository import save_db_info


def db_init(dbms):
    connection_dto = host_port_user_password_db(dbms)
    save_db_info(connection_dto)
    get_connection()
    print('connect success!!')


def host_port_user_password_db(dbms):
    host = typer.prompt('host')
    port = typer.prompt('port')
    user = typer.prompt('user')
    password = typer.prompt('password')
    db = typer.prompt('db')
    return DBConnectionConfig(dbms, host, port, user, password, db)