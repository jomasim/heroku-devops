web: gunicorn run:app
heroku ps:scale web=1
release: python manage.py migrate