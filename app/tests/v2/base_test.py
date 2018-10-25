import json
import unittest
from run import app
from app.schema.create_testing_db import create_testdb,drop_testdb


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        create_testdb()

    def get(self, url):
        return self.client.get(url)

    def post(self, url, data):
        return self.client.post(url,
                                data=json.dumps(data),
                                content_type='application/json')

    def tearDown(self):
        drop_testdb()
