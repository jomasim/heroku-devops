import json
from app.tests.v2.base_test import BaseTestCase

class UserTestCase(BaseTestCase):
    def test_creating_user(self):
        sample_user = {
            'name': 'john doe',
            'email': 'doe@gmail.com',
            'username': 'john',
            'password':'123456'
        }
        response = self.post('/api/v2/user', sample_user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), {
                         'message': 'user created successfully'})
        self.assertEqual(response.mimetype, 'application/json')
