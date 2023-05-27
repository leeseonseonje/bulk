import sys

import typer
from src.app.init.db_connection import DBConnection
from src.app.init.db_connection_config import DBConnectionConfig
from src.app.repository.pickle_db_info_repository import save_db_info


def db_init(dbms):
    db_info = host_port_user_password_db(dbms)
    try:
        connect_db = DBConnection(db_info.host, db_info.port, db_info.user, db_info.password, db_info.db)
        getattr(connect_db, db_info.dbms)()
        save_db_info(db_info)
        print('connect success!!')
    except:
        print('connect failed!!')
        sys.exit(1)


def host_port_user_password_db(dbms):
    host = typer.prompt('host')
    port = typer.prompt('port')
    user = typer.prompt('user')
    password = typer.prompt('password')
    db = typer.prompt('db')
    return DBConnectionConfig(dbms, host, port, user, password, db)