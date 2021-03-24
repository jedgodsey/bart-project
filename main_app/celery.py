import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_app.settings')

app = Celery('main_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_train_1s': {
        'task': 'bart.tasks.get_train',
        'schedule': 5.0
    }
}

app.autodiscover_tasks()
