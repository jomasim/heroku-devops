from app import create_app
from app.schema.db_utils import create_db

app=create_app('development')

if __name__ == '__main__':

    ''' migrate tables '''
    create_db()
    app.run(debug=True)