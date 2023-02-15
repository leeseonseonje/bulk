import typer
import pymysql
from src.repository.pickle_db_info_repository import save_db_info


def mysql(db_name: str):
    init()


def init(db_name: str):
    host = typer.prompt("host")
    port = typer.prompt("port")
    user = typer.prompt("user")
    password = typer.prompt("password")
    db = typer.prompt("db")
    save_db_info(db_name, host, port, user, password, db)
