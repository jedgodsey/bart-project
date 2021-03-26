web: daphne main_app.wsgi:application --port $PORT --bind 0.0.0.0 -v2
worker: celery -A main_app worker -l INFO
beat: celery -A main_app beat -l INFO
