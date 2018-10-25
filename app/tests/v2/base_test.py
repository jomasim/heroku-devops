import json
import unittest
from run import app
from app.schema.create_testing_db import create_testdb,drop_testdb


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        create_testdb()
        ''' create sample login user in test db '''

        create_user_url = "/api/v2/user"
        auth_url = "/api/v2/auth"

        sample_user = {
            'name': 'jane doe',
            'email': 'janedoe@gmail.com',
            'username': 'jane',
            'password':'123456'
        }

        response = self.client.post(create_user_url,
                                    data=json.dumps(sample_user),
                                    content_type='application/json')
        if response.status_code == 201 :

            ''' generate token from sample user if creation was successful '''

            data= {"email": "janedoe@gmail.com", "password": "123456"}

            response = self.client.post(auth_url,
                                        data=json.dumps(data),
                                        content_type='application/json')
            data=json.loads(response.data)
            self.token="Bearer " + data ['access_token']


    def get(self, url):
        return self.client.get(url, headers={"Authorization": self.token})

    def post(self, url, data):
        return self.client.post(url,
                                data=json.dumps(data),
                                content_type='application/json', 
                                headers={"Authorization": self.token})

    def tearDown(self):
        drop_testdb()
