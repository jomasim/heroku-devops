import json
from app.tests.v2.base_test import BaseTestCase


class SaleTestCase(BaseTestCase):
    def test_creating_sale(self):

        ''' sample sale record '''

        new_sale = {
            'id': '1', 
            'date_created': '12/7/2008', 
            'user': 'attendant1',
            'line_items':{
                    'product_id':'1',
                    'item_count':'2',
                    'selling_price':'1200'
            }
        }

        response=self.post('api/v2/sales/',new_sale)
        self.assertEqual(response.mimetype,'application/json')   
        self.assertEqual(response.status_code,201)
        self.assertEqual(json.loads(response.data),{'message':'sale record created successfully'})