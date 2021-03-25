web: celery -A main_app worker -l INFO & celery -A main_app beat -l INFO & gunicorn main_app.asgi --log-file -
