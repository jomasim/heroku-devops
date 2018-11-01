from flask import Flask, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from utils import env
from instance.api_config import api_config
from app.api.v2.views.user_resource import UserController
from app.api.v2.views.auth_resource import AuthController
from app.api.v2.views.product_resource import ProductController
from app.api.v2.views.sale_resource import SalesController
from app.api.v2.views.logout_resource import Logout
from app.api.v2.models.user import User
from app.api.v2.black_list import get_black_list


api_blueprint = Blueprint("store-api", __name__, url_prefix='/api/v2')
jwt = JWTManager()

''' store revoved tokens '''
blacklist = get_black_list()

''' setting api config '''



def create_app(config_setting):
    app = Flask(__name__)
    app.config.from_object(api_config[config_setting])
    app.config['JWT_SECRET_KEY'] = env('JWT_SECRET')
    app.config['JWT_BLACKLIST_ENABLED'] = env('JWT_BLACKLIST')

    jwt.init_app(app)


    ''' setting api blueprint  '''
    api = Api(api_blueprint, catch_all_404s=True)
    api.add_resource(UserController, '/user/',
                     strict_slashes=False, endpoint='post_user')
    api.add_resource(AuthController, '/login/',
                     strict_slashes=False, endpoint='login')

    api.add_resource(Logout, '/logout/',
                     strict_slashes=False, endpoint='logout')

    api.add_resource(ProductController, '/products/',
                     strict_slashes=False, endpoint='products')

    api.add_resource(ProductController, '/products/<int:product_id>/',
                     strict_slashes=False, endpoint='delete/put product')

    api.add_resource(SalesController, '/sales/',
                     strict_slashes=False, endpoint='sales')

    api.add_resource(SalesController, '/sales/<int:sale_id>/',
                     strict_slashes=False, endpoint='get_all_sales')

    app.register_blueprint(api_blueprint)

    return app


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    user_id=identity
    user=User.get_by_id(user_id)
    if user:
        if user['role'] == 'admin':
            return {'roles': 'admin'}
        else:
            return {'roles': 'normal'}

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

def add_to_blacklist(jti):
    return blacklist.add(jti)