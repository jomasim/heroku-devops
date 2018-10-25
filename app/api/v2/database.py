from psycopg2 import connect, sql
from utils import env


class DBConnection():
    @staticmethod
    def __connection():
        host = env('DBHOST')
        user = env('DBUSER')
        name = env('DBNAME')
        password = env('DBPASS')

        return connect(
            host=host,
            user=user,
            password=password,
            dbname=name
        )

    @staticmethod
    def get_connection():
        conn=DBConnection.__connection()
        conn.autocommit=True
        return conn
