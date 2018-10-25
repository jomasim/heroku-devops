from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v2.request import Request
from app.api.v2.models.product import Product


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
        ''' if productid exists in request delete product '''
        if data['product_id']:
            if Product.delete_by_Id(data['product_id']):
                return make_response(jsonify({'message': "product deleted successfully"}), 201)
            return make_response(jsonify({'message': "product does not exist"}), 404)
        else:
            request_schema = {'name': 'required',
                            'category': 'required',
                            'description': 'required',
                            'price': 'required',
                            }

            validator = Request(data, request_schema)
            if validator.validate() == None:

                ''' create product '''
                Product.create(data)

                return make_response(jsonify({'message': "product created successfully"}), 201)
            else:
                return make_response(jsonify(validator.validate()), 422)
