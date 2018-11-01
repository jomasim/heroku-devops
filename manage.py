from app.schema.db_utils import create_db

def migrate():
	return create_db()


migrate()