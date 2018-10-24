import unittest
from app.api.v2.database import DBConnection


class TestDBConnection(unittest.TestCase):
    def test_connection(self):
        connection = DBConnection.get_connection()
        self.assertEqual(0, connection.closed)
