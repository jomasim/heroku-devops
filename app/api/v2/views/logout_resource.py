from flask_jwt_extended import get_raw_jwt
from flask import jsonify, make_response, request
from flask_restful import Resource
from app import blacklist

class Logout(Resource):
    def delete(self):
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        return make_response(jsonify({"message": "Successfully logged out"}), 200)