from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v2.request import Request
from app.api.v2.models.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, jwt_required
import datetime


class AuthController(Resource):
   def post(self):
        data = request.get_json()
        request_schema = {'email': 'required|email',
                          'password': 'required|string|min:6|max:12'}

        validator = Request(data, request_schema)

        if validator.validate() == None:

            email = data['email']
            password = data['password']

            if User.exists({'email':email}):
                user=User.get_by_email(email)
                if check_password_hash(user['password'], password):
                    exp = datetime.timedelta(minutes=20)
                    token = create_access_token(user['email'], exp)
                    return make_response(jsonify({"message": "login successful",
                                                  "access_token": token}), 200)
            return make_response(jsonify({"message": "invalid login"}), 401)
        else:
            return make_response(jsonify(validator.validate()), 422)
