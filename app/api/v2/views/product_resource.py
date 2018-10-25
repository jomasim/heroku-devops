from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v2.request import Request
from app.api.v2.models.product import Product
from flask_jwt_extended import jwt_required, get_jwt_identity


class ProductController(Resource):
    @jwt_required
    def get(self, product_id=None):
        if not product_id:
            return make_response(jsonify({'products': Product.get()}), 200)
        else:

            ''' search for product  using product_id '''

            if not Product.get_by_id(product_id):
                return make_response(jsonify({'error': 'product not found'}), 404)
            else:
                return make_response(jsonify({'product': Product.get_by_id(product_id)}), 200)

    @jwt_required
    def post(self):
        data = request.get_json()
        user = get_jwt_identity()

        ''' append user '''

        data['created_by'] = user

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
