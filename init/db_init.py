import typer
import pymysql

from src.main.app.util.typer_prompt import host_port_user_password_db
from src.main.app.repository.pickle_db_info_repository import save_db_info


class InitDB:

    def __init__(self, name):
        self.name = name

    def mysql(self):
        while True:
            host, port, user, password, db = host_port_user_password_db()
            isCorrect = typer.confirm(f'is your database correct?\n'
                                    f'url: {host}:{port}/{db}\n'
                                    f'id/pw: {user}/{password}\n')
            if isCorrect:
                try:
                    pymysql.connect(host=host, port=int(port), user=user, password=password, db=db, charset='utf8')
                    save_db_info(self.name, host, port, user, password, db)
                    typer.echo('connect success!!')
                except:
                    typer.echo('connect failed!!')
                break


