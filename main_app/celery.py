import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_app.settings')

app = Celery('main_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    # 'get_train_1s': {
    #     'task': 'bart.tasks.get_train',
    #     'schedule': 60
    # },
    'load_delays_1m': {
        'task': 'bart.tasks.load_delays',
        'schedule': 60
    },
    'send_delays_1s': {
        'task': 'bart.tasks.send_delays',
        'schedule': 1
    }
}

app.autodiscover_tasks()
