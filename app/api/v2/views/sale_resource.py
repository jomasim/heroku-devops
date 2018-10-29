from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v2.request import Request
from app.api.v2.models.sale import Sale
from flask_jwt_extended import jwt_required, get_jwt_identity

class SalesController():
    @jwt_required
    def get(self, sale_id=None):
        if not sale_id:
            return make_response(jsonify({'sales': Sale.get()}), 200)
        else:

            ''' search for sale  using sale_id '''

            if not Sale.get_by_id(sale_id):
                return make_response(jsonify({'message': 'sale record not found'}), 404)
            else:
                return make_response(jsonify({'sale': Sale.get_by_id(sale_id)}), 200)

    @jwt_required
    def post(self):
        data = request.get_json()
        user = get_jwt_identity()

        ''' append user '''

        data['created_by'] = user

        all_errors = self.get_validation_errors(data)

        if all_errors == None:

            ''' create sale '''
            Sale.create(data)

            return make_response(jsonify({'message': "sale created successfully"}), 201)
        else:
            return make_response(jsonify(all_errors), 422)
            

    def get_validation_errors(self,data):

        line_items_schema = {'product_id': 'required',
        'item_count':'required','selling_price':'required'
        }
        
        line_items_key_error = Request(data, {'line_items': 'required'})
        line_items_errors=Request(data['line_items'], line_items_schema)
        
        ''' get all general validation errors  '''
        all_errors = dict(line_items_key_error.validate()).copy() 
        all_errors.update(line_items_errors.validate())

        if all_errors==None:

            all_errors={}

            if int(data['line_items']['count']) <= 0:
                all_errors['errors']={"item count":['item count should not be a zero']}
            if int(data['line_items']['selling_price']) <= 0:
                all_errors['errors']={"item count":['item count should not be a zero']}
        
        return all_errors