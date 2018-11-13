from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v2.request import Request
from app.api.v2.models.product import Product
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.v2.views.admin import admin_required

''' collect all key errors '''
key_errors = None


class ProductController(Resource):

    def __init__(self):
        request_schema = {'name': 'required|string',
                          'category': 'required|string',
                          'description': 'required',
                          'price': 'required',
                          'quantity': 'required'
                          }

        self.request_schema=request_schema


    @jwt_required
    def get(self, product_id=None):
        if not product_id:
            return make_response(jsonify({'products': Product.get()}), 200)
        else:

            ''' search for product  using product_id '''

            if not Product.get_by_id(product_id):
                return make_response(jsonify({'message': 'product not found'}), 404)
            else:
                return make_response(jsonify({'product': Product.get_by_id(product_id)}), 200)

    @admin_required
    def post(self):
        data = request.get_json()
        user = get_jwt_identity()

        ''' append user '''

        data['created_by'] = user
        all_errors = self.get_validation_errors(data, self.request_schema)

        if all_errors == None:

            product = Product.get_by_name(data['name'])
            ''' check if product with the same name exists '''
            if product:
                message = "product already exists consider updating the quantity"
                return make_response(jsonify({'message': message}), 409)
            else:
                ''' create product '''
                Product.create(data)

            return make_response(jsonify({'message': "product created successfully"}), 201)
        else:
            return make_response(jsonify(all_errors), 422)

    @admin_required
    def delete(self, product_id=None):
        if not product_id:
              return make_response(jsonify({"message": "productid is required"}), 422)
        else:
            if Product.get_by_id(product_id) != None:
                Product.delete_by_Id(product_id)
                return make_response(jsonify({"message": "product deleted successfully"}), 200)
            else:
                return make_response(jsonify({"message": "product not found"}), 404)

    @admin_required
    def put(self, product_id=None):

        if not product_id:
            return make_response(jsonify({"message": "productid is required"}), 422)

        data = request.get_json()
        user = get_jwt_identity()

        if data != None and not Product.get_by_id(product_id):
            return make_response(jsonify({"message": "product not found"}), 404)

        ''' update product '''
    
        updated_list=self.get_updated_list(data, self.get_existing(product_id))


        ''' collect all errors '''
        
        all_errors=self.validate_update(updated_list,self.get_existing(product_id))
       
        if not all_errors:
            found=self.get_existing(product_id)
            update=all(updated_list[k] == found[k] for k in found)

            if update:
                return make_response(jsonify({"message": "nothing to update"}), 409)

            updated_list['created_by']=user
            Product.update(updated_list, product_id)
            return make_response(jsonify({'message': "product updated successfully"}), 201)

        return make_response(jsonify(all_errors), 422)

    def get_validation_errors(self, data, request_schema):
        validator = Request(data, request_schema)
        all_errors = validator.validate()
        if all_errors == None and int(data['price']) <= 0:
            all_errors = {}
            all_errors['errors'] = {"price": ['price should not be a zero or a negative value']}
        return all_errors


    def get_updated_list(self,data, existing):
    
        sect=[key for key in set(existing) if key in set(data)]
  
        if sect:
            for key in sect:
                existing[key]=data[key]
            
            try:
               existing['quantity']=int(existing['quantity'])
            except ValueError:
                existing['quantity']=0
            return existing

        return None


    def validate_update(self,update,existing):
        all_errors={}
        if update == None:
            all_errors['errors']='invalid request'
            return all_errors
        all_errors = self.get_validation_errors(update,self.request_schema)
        return all_errors

    def get_existing(self,product_id):
        found=Product.get_by_id(product_id)
        found.pop("create_at")
        found.pop("updated_at")
        return found
    