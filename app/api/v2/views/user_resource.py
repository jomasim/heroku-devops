from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v2.request import Request
from app.api.v2.models.user import User
from app.api.v2.views.admin import admin_required


class UserController(Resource):
    @admin_required
    def post(self):

        data = request.get_json()
        request_schema = {'username': 'required|string',
                          'name': 'required|string',
                          'password': 'required|string',
                          'email': 'required|email'
                          }
        validator = Request(data, request_schema)

        if validator.validate() == None:

            ''' check if user exists '''
            if User.exists(data):
                return make_response(jsonify({'message': 'user with email already exists'}), 409)
            else:

                ''' append default role '''

                data['role'] = "normal"

                ''' save user '''
                User.create(data)

                return make_response(jsonify({'message': 'user created successfully'}), 201)
        else:
            return make_response(jsonify(validator.validate()), 422)

    @admin_required
    def get(self):
        return make_response(jsonify({'users':User.get()}),200)