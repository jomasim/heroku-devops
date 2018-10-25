import json
from app.tests.v2.base_test import BaseTestCase
from app.api.v2.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class TestAuth(BaseTestCase):
    def test_for_get_user_identity(self):
        user = User.get_by_email("janedoe@gmail.com")
        self.assertTrue(user)
        self.assertEqual(user['name'], "jane doe")

    def test_match_password(self):
        user = User.get_by_email("janedoe@gmail.com")
        password = "123456"
        self.assertTrue(user)
        self.assertTrue(check_password_hash(user['password'], password))

    def test_login(self):
        user={"email": "janedoe@gmail.com",
            "password": "123456"
                }
        response = self.post('/api/v2/auth', data=user)
        self.assertTrue(response)
        self.assertEqual(response.status_code,200)