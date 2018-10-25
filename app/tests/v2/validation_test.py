from app.api.v2.request import Request
import unittest


class ValidationTest(unittest.TestCase):
    def test_get_field_rules(self):
        string_rules = 'required|min:10|max:20'
        rules = Request.get_field_rules(string_rules)
        self.assertEqual(['required', 'min:10', 'max:20'], rules)

    def test_get_request_rules(self):
        data = {"username": "joma", "password": "1234"}
        request_schema = {'username': 'required|min:10|max:20',
                          'password': 'required|min:10|max:20'}
        request = Request(data, request_schema)
        all_rules = request.get_request_rules()
        self.assertEqual({'password': ['required', 'min:10', 'max:20'],
                          'username': ['required', 'min:10', 'max:20']},
                         all_rules)

    def test_get_value(self):
        data = {"username": "joma", "password": "1234"}
        request_schema = {'username': 'required|min:10|max:20',
                          'password': 'required|min:10|max:20'}
        request = Request(data, request_schema)
        self.assertTrue(request.get_value("username"))
        self.assertFalse(request.get_value("name"))
        self.assertEqual("joma", request.get_value("username"))

    def test_validate_field(self):
        data = {"username": "", "password": "1234"}
        request_schema = {'username': 'required|min:10|max:20',
                          'password': 'required|min:10|max:20',
                          }
        request = Request(data, request_schema)
        field_rules = ['required', 'min:10', 'max:20']
        field = "username"
        errors = request.validate_field(field, field_rules)
        self.assertEqual(['username is required'], errors)

    def test_validate_request(self):
        data = {"username": "", "password": "1234"}
        request_schema = {'username': 'required',
                          'password': 'required',
                          'name': 'required',
                          }
        request = Request(data, request_schema)
        self.assertTrue(request.validate())
        self.assertEqual({'errors': {'username': ['username is required'],
                                     'name': ['name is required']}},
                         request.validate())

    def test_valid_request(self):
        data = {"username": "joma", "password": "1234", "name": "joma simeon"}
        request_schema = {'username': 'required',
                          'password': 'required',
                          'name': 'required',
                          }
        request = Request(data, request_schema)
        self.assertEqual(None, request.validate())

    def test_get_rule_argument(self):
        string_rules = 'required|min:10|max:20'
        rules = Request.get_field_rules(string_rules)
        arg1 = Request.get_rule_argument("min", rules)
        arg2 = Request.get_rule_argument("max", rules)
        self.assertEqual("10", arg1)
        self.assertEqual("20", arg2)

    def test_get_non_existing_rule_arg(self):
        string_rules = 'required|min:10|max:20'
        rules = Request.get_field_rules(string_rules)
        arg = Request.get_rule_argument("maxc", rules)
        self.assertEqual(None, arg)

    def test_for_min_length(self):
        data = {"username": "joma", "password": "1234", "name": "joma simeon"}
        request_schema = {'username': 'required|min:10|max:20',
                          'password': 'required|min:10|max:20',
                          'name': 'required|min:10|max:20',
                          }
        request = Request(data, request_schema)
        self.assertEqual({'errors': {
            'username': ['username should have a minimum of 10 characters'],
            'password': ['password should have a minimum of 10 characters']}},
            request.validate())

    def test_for_max_length(self):
        data = {"username": "jomasim",
                "password": "12340454", "name": "joma simeon"}
        request_schema = {'username': 'required|max:5',
                          'password': 'required|max:20',
                          'name': 'required|string|min:4|max:7',
                          }
        request = Request(data, request_schema)
        self.assertEqual({'errors': {
            'name': ['name should have a maximum of 7 characters'],
            'username': ['username should have a maximum of 5 characters']
        }}, request.validate())

    def test_invalid_string(self):
        data = {"username": "jomasim", "password": "12340454", "name": 9}
        request_schema = {'username': 'required|max:13',
                          'password': 'required|max:20',
                          'name': 'required|string|min:1|max:7',
                          }
        request = Request(data, request_schema)
        self.assertEqual({'errors': {
            'name': ['name should be a string']}}, request.validate())

    def test_mixed_violation(self):
        data = {"username": "jomasim", "password": "12340454", "name": 9}
        request_schema = {'username': 'required|max:5',
                          'password': 'required|max:20',
                          'name': 'required|string|min:4|max:7',
                          }
        request = Request(data, request_schema)
        self.assertEqual({'errors': {
            'username': ['username should have a maximum of 5 characters'],
            'name': ['name should be a string', 'name should have a minimum of 4 characters']}},
            request.validate())
