import sys

sys.path.insert(0, '../../../')
from src.main.app.init.db_init import InitDB
from src.main.app.repository.pickle_db_info_repository import load_db_info
import typer

app = typer.Typer()


@app.command()
def init(db_name: str = typer.Argument('mysql')):
    init_db = InitDB(db_name.lower())
    getattr(init_db, init_db.name)()


@app.command()
def load():
    typer.echo(load_db_info())
