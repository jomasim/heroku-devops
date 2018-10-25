import json
from tests.base_test import BaseTestCase


class ProductTestCase(BaseTestCase):
    def test_creating_product(self):
        new_product = {'id':'1','name': 'shirt', 'category': 'apparel', 'description': {
            'color': 'black',
            'size': '35',
            'gender': 'male'
        }, 'price': '1200'}
        response = self.post('/api/v2/products', data=new_product)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.mimetype,'application/json')

    def test_for_empty_data(self):
        response=self.post('/api/v2/products', data={})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.mimetype,'application/json')
    
    

