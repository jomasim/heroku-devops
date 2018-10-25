from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v2.request import Request

class ProductController(Resource):
    def get(self, product_id=None):
        if not product_id:
            return make_response(jsonify({'products': products}), 200)
        else:

            ''' search for product  using product_id '''

            product = [
                product for product in products if product['id'] == str(product_id)]
            if not product:
                return make_response(jsonify({'error': 'product not found'}), 404)
            else:
                return make_response(jsonify({'product': product}), 200)

    def post(self):
        data = request.get_json()
        request_schema = {'name': 'required',
                          'category': 'required',
                          'description':'required',
                          'price':'required',
                          'quantity':'required'
                          }
        validator=Request(data, request_schema)
        if validator.validate() == None :
            if not data:
                return make_response(jsonify({'error': 'invalid data'}), 422)
            product_id = len(products)+1
            product = {'id': product_id, 'name': data['name'], 'category': data['category'],
                    'description': data['description'],
                    'price': data['price'], 'quantity': data['quantity']
                    }
            products.append(product)
            return make_response(jsonify({'products': products}), 201)
        else:
            return make_response(jsonify(validator.validate()), 422)