worker: celery -A main_app worker -l INFO
beat: celery -A main_app beat -l INFO
web: gunicorn main_app.wsgi --log-file -
