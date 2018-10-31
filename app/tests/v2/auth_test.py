import json
from app.tests.v2.base_test import BaseTestCase
from app.api.v2.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class TestAuth(BaseTestCase):
    def test_for_get_user_identity(self):
        user = User.get_by_email(self.sample_user['email'])
        self.assertTrue(user)
        self.assertEqual(user['name'], self.sample_user['name'])

    def test_match_password(self):
        user = User.get_by_email(self.sample_user['email'])
        password = "123456"
        self.assertTrue(user)
        self.assertTrue(check_password_hash(user['password'], password))

    def test_login(self):
        user={"email": self.sample_user['email'],
            "password":self.sample_user['password'],
                }
        response = self.post('/api/v2/login', data=user)
        self.assertTrue(response)
        data=json.loads(response.data)
        self.assertEqual({"message":data['message']}, {
                         'message': 'login successful'})
        self.assertEqual(response.status_code,200)

    def test_login_with_invalid_credentials(self):
        user={"email": "kimdoe@gmail.com",
            "password": "1234566343"
                }
        response = self.post('/api/v2/login', data=user)
        self.assertTrue(response)
        self.assertEqual(json.loads(response.data), {
                         'message': 'invalid login'})
        self.assertEqual(response.status_code,401)

    def test_login_with_empty_data(self):
        user={"email": "",
            "password": ""
                }
        response = self.post('/api/v2/login', data=user)
        self.assertTrue(response)
        self.assertEqual(json.loads(response.data), 
        {'errors': {'email': ['email is required'],
        'password': ['password is required']}})
        self.assertEqual(response.status_code,422)
