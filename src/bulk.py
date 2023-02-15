import sys
sys.path.insert(0, '../')

import typer
from src.init.db_init import mysql

app = typer.Typer()


@app.command()
def init(db_name: str = 'mysql'):
    init_function = db_name + '(' + "'" + db_name + "'" + ')'
    eval(init_function)


@app.command()
def query(query: str):
    print(query)
