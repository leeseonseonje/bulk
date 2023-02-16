from enum import Enum
import typer

from src.repository.pickle_db_info_repository import save_db_info



def mysql():
    host = typer.prompt("host")
    port = typer.prompt("port")
    user = typer.prompt("user")
    password = typer.prompt("password")
    db = typer.prompt("db")
    save_db_info('mysql', host, port, user, password, db)


class DBType(Enum):
    MYSQL = mysql()
    POSTGRESQL = 'postgresql'
    SQLITE = 'sqlite'