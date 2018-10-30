from flask import Flask, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from utils import env
from instance.api_config import api_config
from app.api.v2.views.user_resource import UserController
from app.api.v2.views.auth_resource import AuthController
from app.api.v2.views.product_resource import ProductController
from app.api.v2.views.sale_resource import SalesController

api_blueprint = Blueprint("store-api", __name__, url_prefix='/api/v2')
jwt = JWTManager()

''' setting api config '''


def create_app(config_setting):
    app = Flask(__name__)
    app.config.from_object(api_config[config_setting])
    app.config['JWT_SECRET_KEY'] = env('JWT_SECRET')

    jwt.init_app(app)

    ''' setting api blueprint  '''
    api = Api(api_blueprint)
    api.add_resource(UserController, '/user/',
                     strict_slashes=False, endpoint='post_user')
    api.add_resource(AuthController, '/login/',
                     strict_slashes=False, endpoint='login')

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
