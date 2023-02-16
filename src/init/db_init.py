import typer


class InitDB:

    def __init__(self, name):
        self.name = name

    def mysql(self):
        host = typer.prompt("host")
        port = typer.prompt("port")
        user = typer.prompt("user")
        password = typer.prompt("password")
        db = typer.prompt("db")
        # save_db_info(self.name, host, port, user, password, db)

