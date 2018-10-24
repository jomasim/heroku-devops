from app.api.v2.database import DBConnection
from werkzeug.security import generate_password_hash
from psycopg2 import sql

cur = DBConnection.get_connection().cursor()


class User(object):
   
    ''' create user '''
    @staticmethod
    def create_user(data):
        query = sql.SQL("insert into {} ({}) values ({})").format(
            sql.Identifier("users"),
            sql.SQL(', ').join(map(sql.Identifier, data.keys())),
            sql.SQL(', ').join(sql.Placeholder() * len(data))
        )
        cur.execute(query, data.values())
     
