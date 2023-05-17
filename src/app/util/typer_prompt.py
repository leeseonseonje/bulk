import typer

from src.app.init.db_connection_dto import DBConnectionDto


def host_port_user_password_db(dbms):
    host = typer.prompt('host')
    port = typer.prompt('port')
    user = typer.prompt('user')
    password = typer.prompt('password')
    db = typer.prompt('db')
    return DBConnectionDto(dbms, host, port, user, password, db)


def entered_db_information(host='', port='', db='', user='', password=''):
    if host:
        return typer.confirm(f'is your database correct?\n'
                      f'url: {host}:{port}/{db}\n'
                      f'id/pw: {user}/{password}\n')
    else:
        return typer.confirm(f'is your database correct?\n'
                      f'db: {db}')









