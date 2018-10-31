import json
import unittest
from run import app
from app.schema.db_utils import create_db, drop_db
from app.api.v2.models.user import User
from app.api.v2.models.product import Product
from app.api.v2.models.sale import Sale



sample_user = {
            'name': 'support',
            'email': 'support@gmail.com',
            'username': 'support',
            'password': '123456'
        }
sample_product = {'name': 'trouser', 'category': 'apparel',
                           'description': {
                               'color': 'grey',
                               'size': '35',
                               'gender': 'male'
                           }, 'price': '1500'}
sale = {
        'line_items': {
                    'product_id': '1',
                    'item_count': '2',
                    'selling_price': '1700'
                }
        }

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        self.sample_user=sample_user
        self.sample_product=sample_product
        self.sample_sale=sale

        # create database tabless
        create_db()

        login_url = "/api/v2/login"
        product_url = "/api/v2/products"
        sale_url = "/api/v2/sales"
        
        ''' create defualt admin '''
        User.create_admin(self.sample_user)
        if User.exists(sample_user):

            ''' generate token from sample user if creation was successful '''

            data = {"email": "support@gmail.com", "password": "123456"}

            response = self.client.post(login_url,
                                        data=json.dumps(data),
                                        content_type='application/json')
            data = json.loads(response.data)
        
            self.token = "Bearer " + data['access_token']


            ''' create sample product '''
            self.client.post(
                product_url,
                data=json.dumps(sample_product),
                content_type='application/json',
                headers={"Authorization": self.token}
            )

            ''' create sample sale '''
            self.client.post(
                sale_url,
                data=json.dumps(self.sample_sale),
                content_type='application/json',
                headers={"Authorization": self.token}
            )

            

    def get(self, url):
        return self.client.get(url, headers={"Authorization": self.token})

    def post(self, url, data):
        return self.client.post(url,
                                data=json.dumps(data),
                                content_type='application/json',
                                headers={"Authorization": self.token})

    def put(self, url, data):
        return self.client.put(
            url,
            data=json.dumps(data),
            content_type='application/json',
            headers={"Authorization": self.token}
        )

    def delete(self, url):
        return self.client.delete(url, headers={"Authorization": self.token})

    def tearDown(self):
        drop_db()
