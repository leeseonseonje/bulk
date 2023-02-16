import typer


def host_port_user_password_db():
    host = typer.prompt("host")
    port = typer.prompt("port")
    user = typer.prompt("user")
    password = typer.prompt("password")
    db = typer.prompt("db")
    return host, port, user, password, db



