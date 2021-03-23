import requests

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task

channel_layer = get_channel_layer()

@shared_task
def get_train():
    url = 'https://api.bart.gov/api/etd.aspx?cmd=etd&orig=all&key=MW9S-E7SL-26DU-VV8V&json=y'
    response = requests.get(url).json()
    train = response['root']['station'][0]['name']
    
    async_to_sync(channel_layer.group_send)('trains', {'type': 'send_trains', 'text': train})
