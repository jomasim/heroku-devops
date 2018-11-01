from app.api.v2.database import DBConnection
from psycopg2 import sql, extras
import json


cur = DBConnection.get_connection().cursor(cursor_factory=extras.RealDictCursor)

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
            sale=cur.fetchone()
            if sale:
                sale['line_items'] = json.loads(sale['line_items'])
            return sale
        return False


    ''' returns all sales '''
    
    @staticmethod
    def get():
        query = "SELECT * FROM sales"
        cur.execute(query)
        sales = cur.fetchall()
        for i, sale in enumerate(sales):
            sales[i]['line_items'] = json.loads(sale['line_items'])
        return sales
    
    @staticmethod
    def update(data,sale_id):
        query="UPDATE sales SET created_by='%s',line_items='%s' WHERE id='%s' " %(
        data['created_by'],json.dumps(data['description']),sale_id)
        return cur.execute(query)