import typer

from src.repository.pickle_db_info_repository import db_info_save


def mysql():
    host = typer.prompt("host")
    port = typer.prompt("port")
    user = typer.prompt("user")
    password = typer.prompt("password")
    db = typer.prompt("db")
    db_info_save(host, port, user, password, db)