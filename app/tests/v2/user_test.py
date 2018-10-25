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

    def test_for_existing_user(self):
        existing_user = {
            'name': 'jane doe',
            'email': 'janedoe@gmail.com',
            'username': 'jane',
            'password':'123456'
        }
        response = self.post('/api/v2/user', existing_user)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(json.loads(response.data), {
                         'message': 'user with email already exists'})
        self.assertEqual(response.mimetype, 'application/json')
        
    def test_for_empty_data(self):
        response = self.post('/api/v2/user', data={})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.mimetype, 'application/json')