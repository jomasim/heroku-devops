from app.api.v2.database import DBConnection
from werkzeug.security import generate_password_hash
from psycopg2 import sql,extras



cur = DBConnection.get_connection().cursor(cursor_factory = extras.RealDictCursor)

class User(object):

    ''' create user '''
    @staticmethod
    def create(data):
        hashed=generate_password_hash(data['password'])
        query = "INSERT INTO users (name,username,email,password,role)" \
                "VALUES('%s','%s', '%s', '%s', '%s')" % (
                    data['name'],data['username'],data['email'],hashed,data['role'])
        cur.execute(query)

    @staticmethod
    def create_admin(data):
        hashed=generate_password_hash(data['password'])
        query = "INSERT INTO users (name,username,email,password,role)" \
                "VALUES('%s','%s', '%s', '%s', '%s')" % (
                    data['name'],data['username'],data['email'],hashed,"admin")
        cur.execute(query)

    @staticmethod
    def exists(data):
        if data['email']:
            query="SELECT * FROM users WHERE email = '%s';" % data['email']
            cur.execute(query)
            return cur.fetchone()
        return False

    @staticmethod
    def get_by_email(email):
        if email:
            query="SELECT * FROM users WHERE email = '%s';" % email
            cur.execute(query)
            return cur.fetchone()
            
    @staticmethod
    def get_by_id(user_id):
        if user_id:
            query="SELECT * FROM users WHERE id = '%s';" % user_id
            cur.execute(query)
            return cur.fetchone()

    @staticmethod
    def get():
        query="SELECT * FROM users"
        cur.execute(query)
        users=cur.fetchall()

        for user in users:
            user.pop("password")

        return users
