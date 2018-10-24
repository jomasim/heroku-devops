from app.api.v2.database import DBConnection
from werkzeug.security import generate_password_hash

cur = DBConnection.get_connection().cursor()


class User(object):
    def __init__(self, name, email, username, password):

        self.id = "",
        self.name = name,
        self.email = email,
        self.username = username,
        self.password = password
        self.role = None

    ''' create user '''

    def create(self):
        query = "INSERT INTO " \
            "users (name,username,email,password,role)" \
            "VALUES('%s','%s','%s','%s','%s')" % (
                self.name, self.username, self.email, self.password, self.role)
        cur.execute(query)
        cur.commit()
    
