from app.api.v2.database import DBConnection
import psycopg2.extras


cur = DBConnection.get_connection().cursor(
    cursor_factory=psycopg2.extras.DictCursor)


class Product(object):

    ''' create product '''
    @staticmethod
    def create(data):

        query = "INSERT INTO products (name,category,description,price,user)" \
                "VALUES('%s','%s', '%s', '%s', '%s')" % (
                    data['name'], data['category'], data['price'], data['description'], data['create_by'])
        cur.execute(query)

    @staticmethod
    def delete_by_Id(product_id):
        if product_id:
            query = "DELETE * FROM products WHERE id = '%s';" % product_id
            cur.execute(query)
        return False

    @staticmethod
    def get_by_id(product_id):
        if product_id:
            query = "SELECT * FROM products WHERE id = '%s';" % product_id
            cur.execute(query)
            return cur.fetchone()
        return False

    @staticmethod
    def update(payload, id):
        pass
