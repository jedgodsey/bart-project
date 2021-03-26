redis: cd redis-stable & make MALLOC=libc & src/redis-server
worker: celery -A main_app worker -l INFO
beat: celery -A main_app beat -l INFO
web: gunicorn main_app.asgi --log-file -
