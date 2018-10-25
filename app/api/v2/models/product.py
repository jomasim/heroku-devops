from app.api.v2.database import DBConnection
from psycopg2 import sql
import psycopg2.extras
import json


cur = DBConnection.get_connection().cursor(cursor_factory = psycopg2.extras.DictCursor)

class Product(object):

    ''' create product '''
    @staticmethod
    def create(data):

        query = "INSERT INTO products (name,category,description,price,created_by)" \
                "VALUES('%s','%s', '%s', '%s', '%s')" % (
                    data['name'], data['category'], data['price'], json.dumps(data['description']), data['created_by'])
        cur.execute(query)

    @staticmethod
    def delete_by_Id(product_id):
        if product_id:
            query = "DELETE  FROM products WHERE id = '%s';" % product_id
            cur.execute(query)
        return False

    @staticmethod
    def get_by_id(product_id):
        if product_id:
            query = "SELECT * FROM products WHERE id = '%s';" % product_id
            cur.execute(query)
            return cur.fetchone()
        return False

    ''' returns all products '''
    
    @staticmethod
    def get():
        query = "SELECT * FROM products"
        cur.execute(query)
        return cur.fetchall()

    @staticmethod
    def update(data,product_id):
        query="UPDATE products SET name='%s',category='%s',description='%s',price='%s',created_by='%s' WHERE id='%s' " %(
        data['name'], data['category'],json.dumps(data['description']),data['price'],  data['created_by'],product_id)
        return cur.execute(query)
        
       
        
