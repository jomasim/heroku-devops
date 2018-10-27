from app.api.v2.database import DBConnection
import os

ROOTDIRECTORY=os.path.dirname(os.path.abspath(__file__))

cur=DBConnection.get_connection().cursor()
drop_query_file=ROOTDIRECTORY + "/createdb.sql"
create_query_file= path=ROOTDIRECTORY + "/dropdb.sql"

def create_db():
    return cur.execute(open(create_query_file, 'r').read())

def drop_db():
    return cur.execute(open(drop_query_file, 'r').read())