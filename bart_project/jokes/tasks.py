import requests

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task

channel_layer = get_channel_layer()

@shared_task
def get_joke():
    url = 'http://api.icndb.com/jokes/random/'
    response = requests.get(url).json()
    joke = response['value']['joke']
    
    async_to_sync(channel_layer.group_send)('jokes', {'type': 'send_jokes', 'text': joke})
