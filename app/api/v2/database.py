from psycopg2 import connect, sql
from utils import env
from sys import modules


class DBConnection():
    @staticmethod
    def __connection():

        if 'pytest' in modules:
            host = env('TESTING_DBHOST')
            user = env('TESTING_DBUSER')
            name = env('TESTING_DBNAME')
            password = env('TESTING_DBPASS')
        else:
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



