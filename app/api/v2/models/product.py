from app.api.v2.database import DBConnection
from psycopg2 import sql,extras
import json


cur = DBConnection.get_connection().cursor(cursor_factory = extras.RealDictCursor)

class Product(object):

    ''' create product '''
    @staticmethod
    def create(data):

        query = "INSERT INTO products (name,category,description,price,quantity,created_by)" \
                "VALUES('%s','%s', '%s', '%s','%s', '%s')" % (
                    data['name'], data['category'],json.dumps(data['description']),data['price'],data['quantity'], data['created_by'])
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
            product=cur.fetchone()
            if product:
                product['description'] = json.loads(product['description'])
            return product
        return False

    @staticmethod
    def get_by_name(product_name):
        if product_name:
            query = "SELECT * FROM products WHERE name = '%s';" % product_name
            cur.execute(query)
            product=cur.fetchone()
            if product:
                product['description'] = json.loads(product['description'])
            return product
        return False


    ''' returns all products '''
    
    @staticmethod
    def get():
        query = "SELECT * FROM products"
        cur.execute(query)
        products=cur.fetchall()
        for i, product in enumerate(products):
            products[i]['description'] = json.loads(product['description'])
        return products

    @staticmethod
    def update(data,product_id):
        query="UPDATE products SET name='%s',category='%s',description='%s',price='%s',quantity='%s',created_by='%s' WHERE id='%s' " %(
        data['name'], data['category'],json.dumps(data['description']),data['price'],data['quantity'], data['created_by'],product_id)
        return cur.execute(query)
        
       
        
