import json
from app.tests.v2.base_test import BaseTestCase


class SaleTestCase(BaseTestCase):
    def test_creating_sale(self):
        ''' sample sale record '''

        new_sale = {
            'line_items':[{
                    'product_id': '1',
                    'item_count': '2',
                    'selling_price': '1200'
            },
            {
                    'product_id': '1',
                    'item_count': '2',
                    'selling_price': '1200'
            },
            ]
            }

        response = self.post('api/v2/sales/', new_sale)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), {
                         'message': 'sale created successfully'})

    def test_creating_sale_with_zero_item_count(self):
        ''' sample sale record '''

        new_sale = {
            'line_items':[{
                    'product_id': '1',
                    'item_count': '0',
                    'selling_price': '1200'
            },
            {
                    'product_id': '1',
                    'item_count': '0',
                    'selling_price': '1200'
            },
            ]
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
            'line_items':[{
                    'product_id': '1',
                    'item_count': '2',
                    'selling_price': '0'
            },
            {
                    'product_id': '1',
                    'item_count': '2',
                    'selling_price': '0'
            },
            ]
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

    def test_get_all_sales(self):
        response=self.get('/api/v2/sales/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.mimetype,'application/json')

    def test_get_specific_sale(self):
        response=self.get('/api/v2/sales/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.mimetype,'application/json')

    def test_get_non_exisiting_sale_record(self):
        response=self.get('/api/v2/sales/10008')
        self.assertEqual(response.status_code,404)
        self.assertEqual(json.loads(response.data), {
                         'message': 'sale record not found'})
        self.assertEqual(response.mimetype,'application/json')

    def test_sale_more_than_in_stock(self):
        new_sale = {
            'line_items': [{
                'product_id': '1',
                'item_count': '10',
                'selling_price': '1700'
            }, ]}
        response = self.post('/api/v2/sales', new_sale)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(json.loads(response.data),
                         {'errors': {'stock': ['cant sell more than in stock for product id: 1']}
                          })
        self.assertEqual(response.mimetype, 'application/json')
