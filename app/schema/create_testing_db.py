from app.api.v2.database import DBConnection
import os

ROOTDIRECTORY=os.path.dirname(os.path.abspath(__file__))

cur=DBConnection.get_connection().cursor()

def create_testdb():
    path=ROOTDIRECTORY + "/createdb.sql"
    return cur.execute(open(path, 'r').read())

def drop_testdb():
    path=ROOTDIRECTORY + "/dropdb.sql"
    return cur.execute(open(path, 'r').read())