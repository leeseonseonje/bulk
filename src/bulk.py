import sys
sys.path.insert(0, '../')

import typer

app = typer.Typer()


@app.command()
def init(db_name: str = 'mysql'):
    eval(db_name + '()')


@app.command()
def query(query: str):
    print(query)
