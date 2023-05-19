from src.app.init.db_connection import DBConnection
import pymysql
import psycopg2


def test_mysql_connection():
    connect_db = DBConnection('localhost', '3306', 'root', 'root', 'cli_test')
    mysql_connect = getattr(connect_db, 'mysql')()
    assert type(mysql_connect) == pymysql.connections.Connection


def test_postgres_connection():
    connect_db = DBConnection('localhost', '5432', 'postgres', '1234', 'test')
    postgres_connect = getattr(connect_db, 'postgres')()
    assert type(postgres_connect) == psycopg2.extensions.connection

