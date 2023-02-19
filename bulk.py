import sys
sys.path.insert(0, '../../../')
from src.main.app.init.db_init import InitDB
from src.main.app.repository.pickle_db_info_repository import load_db_info
from src.main.app.db.query_execute import __sql__
from src.main.app.db.bulk_insert import bulk_insert
import typer

app = typer.Typer()


@app.command()
def init(db_name: str = typer.Argument('mysql')):
    try:
        init_db = InitDB(db_name.lower())
        getattr(init_db, init_db.name)()
    except:
        print(f'{db_name.lower()} is not db')


@app.command()
def load():
    print(load_db_info())


@app.command()
def sql(query: str):
    __sql__(query)


@app.command()
def bulk(table: str, row: int = typer.Option(1)):
    bulk_insert(table, row)


