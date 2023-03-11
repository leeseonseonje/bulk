import sys
from pathlib import Path


sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from src.main.app.init.db_init import InitDB
from src.main.app.repository.pickle_db_info_repository import load_db_info, load_db_name
from src.main.app.query.query_execute import __sql__
from src.main.app.bulk.bulk_insert import BulkInsert
from src.main.app.query.delete_table import delete_table
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
def bulk(table: str,
         row: int = typer.Option(1),
         rm: bool = typer.Option(False),
         ran: bool = typer.Option(False)):
    if rm:
        delete_table(table)
    insert = BulkInsert(table, row, ran)
    getattr(insert, load_db_name())()


if __name__ == "__main__":
    app()