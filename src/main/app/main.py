import sys
from pathlib import Path


sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from src.main.app.init.db_connection_dto import DBConnectionDto
from src.main.app.init.db_init import db_init
from src.main.app.repository.pickle_db_info_repository import load_db_info
from src.main.app.query.query_execute import __sql__
from src.main.app.bulk.bulk_insert import BulkInsert
import typer

app = typer.Typer()


@app.command()
def init(dbms: str = typer.Argument('mysql')):
    db_init(dbms)


@app.command()
def load():
    db_info: DBConnectionDto = load_db_info()
    print(f'dbms: {db_info.dbms}')
    print(f'host/port: {db_info.host}/{db_info.port}')
    print(f'user/password: {db_info.user}/{db_info.password}')
    print(f'db: {db_info.db}')


@app.command()
def sql(query: str):
    __sql__(query)


@app.command()
def bulk(table: str,
         row: int = typer.Option(1),
         ran: bool = typer.Option(False)):
    insert = BulkInsert(table, row, ran)
    getattr(insert, load_db_info().dbms)()


if __name__ == "__main__":
    app()
