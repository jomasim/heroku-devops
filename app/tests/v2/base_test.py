import json
import unittest
from run import app
from app.schema.db_utils import create_db, drop_db


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        create_db()
        ''' create sample login user in test db '''

        create_user_url = "/api/v2/user"
        auth_url = "/api/v2/auth"
        product_url="/api/v2/products"

        sample_user = {
            'name': 'jane doe',
            'email': 'janedoe@gmail.com',
            'username': 'jane',
            'password': '123456'
        }

        response = self.client.post(create_user_url,
                                    data=json.dumps(sample_user),
                                    content_type='application/json')
        if response.status_code == 201:

            ''' generate token from sample user if creation was successful '''

            data = {"email": "janedoe@gmail.com", "password": "123456"}

            response = self.client.post(auth_url,
                                        data=json.dumps(data),
                                        content_type='application/json')
            data = json.loads(response.data)
            self.token = "Bearer " + data['access_token']

            ''' create sample products '''

            'sample product 1'

            product = {'id': '1', 'name': 'trouser', 'category': 'apparel',
                           'description': {
                               'color': 'grey',
                               'size': '35',
                               'gender': 'male'
                           }, 'price': '1500'}
        
            self.client.post(product_url,
                    data=json.dumps(product),
                    content_type='application/json',
                    headers={"Authorization": self.token})

            ''' sample product 2 '''

            product2 = {'id': '2', 'name': 'ladies jeans', 'category': 'apparel',
                           'description': {
                               'color': 'grey',
                               'size': '37',
                               'gender': 'female'
                           }, 'price': '1800'}

            self.client.post(product_url,
                    data=json.dumps(product2),
                    content_type='application/json',
                    headers={"Authorization": self.token})

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
