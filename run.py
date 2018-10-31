from app import create_app
from app.schema.db_utils import create_db
from app.api.v2.models.user import User

admin = {
            'name': 'support',
            'email': 'support@gmail.com',
            'username': 'support',
            'password': '123456'
        }


app=create_app('development')

if __name__ == '__main__':

    ''' migrate tables '''
    create_db()
    # creating admin when starting app if the admin does not exist
    if not User.exists(admin):
        User.create_admin(admin)
    app.run(debug=True)