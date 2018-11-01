from app.api.v2.database import DBConnection
from psycopg2 import sql
import psycopg2.extras
import json


cur = DBConnection.get_connection().cursor(cursor_factory = psycopg2.extras.DictCursor)

class Sale():
    ''' create sale '''
    @staticmethod
    def create(data):

        query = "INSERT INTO sales (created_by,line_items)" \
                "VALUES('%s', '%s')" % (data['created_by'],json.dumps(data['line_items']))
        return cur.execute(query)
    
    @staticmethod
    def get_by_id(sale_id):
        if sale_id:
            query = "SELECT * FROM sales WHERE id = '%s';" % sale_id
            cur.execute(query)
            return cur.fetchone()
        return False


    ''' returns all sales '''
    
    @staticmethod
    def get():
        query = "SELECT * FROM sales"
        cur.execute(query)
        return cur.fetchall()
    
    @staticmethod
    def update(data,sale_id):
        query="UPDATE sales SET created_by='%s',line_items='%s' WHERE id='%s' " %(
        data['created_by'],json.dumps(data['description']),sale_id)
        return cur.execute(query)