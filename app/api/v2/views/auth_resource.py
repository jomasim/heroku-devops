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

            ''' verify password '''
            if AuthController.__verify_password(email,password):
                user=User.get_by_email(email)
                exp = datetime.timedelta(minutes=45)
                token=AuthController.__generate_token(user['id'],exp)
                user.pop("password")
                return make_response(jsonify({"message": "Login successful",
                                                  "access_token": token,
                                                  "exp":str(exp),
                                                  "user":user}), 200)
            else:                                    
                return make_response(jsonify({"message": "Invalid credentials"}), 401)
        else:
            return make_response(jsonify(validator.validate()), 422)

    @staticmethod
    def __generate_token(user_id,exp):
        return create_access_token(user_id, exp)

    @staticmethod
    def __verify_password(email,password):
        if User.exists({'email':email}):
            user=User.get_by_email(email)
            return check_password_hash(user['password'], password)
        return False
                

