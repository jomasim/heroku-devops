import json
from app.tests.v2.base_test import BaseTestCase


class SaleTestCase(BaseTestCase):
    def test_creating_sale(self):
        ''' sample sale record '''

        new_sale = {
            'id': '1',
            'date_created': '12/7/2008',
            'user': 'attendant1',
            'line_items': {
                    'product_id': '1',
                    'item_count': '3',
                    'selling_price': '1200'
            }
        }

        response = self.post('api/v2/sales/', new_sale)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), {
                         'message': 'sale created successfully'})

    def test_creating_sale_with_zero_item_count(self):
        ''' sample sale record '''

        new_sale = {
            'id': '1',
            'date_created': '12/7/2008',
            'user': 'attendant1',
            'line_items': {
                    'product_id': '1',
                    'item_count': '0',
                    'selling_price': '1200'
            }
        }

        response = self.post('api/v2/sales/', new_sale)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual(response.status_code, 422)
        self.assertEqual(json.loads(response.data), {'errors':
                                                     {'item count': [
                                                         'item count should not be a zero']}
                                                     })
    def test_creating_sale_with_zero_selling_price(self):
        ''' sample sale record '''

        new_sale = {
            'id': '1',
            'date_created': '12/7/2008',
            'user': 'attendant1',
            'line_items': {
                    'product_id': '1',
                    'item_count': '2',
                    'selling_price': '0'
            }
        }

        response = self.post('api/v2/sales/', new_sale)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual(response.status_code, 422)
        self.assertEqual(json.loads(response.data), {'errors':
                                                     {'selling price': [
                                                         'selling price should not be a zero']}
                                                     })

    def test_creating_sale_with_empty_data(self):
        response = self.post('/api/v2/sales', data={})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(json.loads(response.data),
                         {'errors': {'item_count': ['item_count is required'],
                                     'product_id': ['product_id is required'],
                                     'selling_price': ['selling_price is required']}
                          })
        self.assertEqual(response.mimetype, 'application/json')
