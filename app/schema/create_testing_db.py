from app.api.v2.database import TestingDB

cur=TestingDB.get_connection().cursor()

def create_testdb():
    cur.execute(open(('createdb.sql'), 'r').read())

def drop_testdb():
    cur.execute(open(('dropdb.sql'), 'r').read())