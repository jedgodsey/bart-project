worker1: celery -A main_app worker -l INFO
worker2: celery -A main_app beat -l INFO
web: gunicorn main_app.asgi --log-file -
