from flask_jwt_extended import (verify_jwt_in_request,get_jwt_claims)
from functools import wraps
from flask import jsonify, make_response


# decorater checks if request has jwt token and user has role admin
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['roles'] != 'admin':
             return make_response(jsonify({'message': 'admin required'}), 403)
        else:
            return fn(*args, **kwargs)
    return wrapper


