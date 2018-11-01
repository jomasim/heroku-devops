from flask_jwt_extended import get_raw_jwt,jwt_required
from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v2.black_list import add_to_black_list


class Logout(Resource):
	@jwt_required
	def delete(self):
		jti = get_raw_jwt()['jti']
		add_to_black_list(jti)
		return make_response(jsonify({"message": "Successfully logged out"}), 200)