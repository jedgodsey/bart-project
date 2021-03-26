import requests
from functools import reduce
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task
from .models import Delays
from django.core import serializers


channel_layer = get_channel_layer()

@shared_task
def load_delays():
    url = 'https://api.bart.gov/api/etd.aspx?cmd=etd&orig=all&key=MW9S-E7SL-26DU-VV8V&json=y'
    response = requests.get(url).json()
    train = response['root']['station'][0]['name']
    stations = response['root']['station']
    def get_delays(n):
        total = 0
        number = 0
        for i in n['etd']:
            total = total + int(i['estimate'][0]['delay'])
            number = number + 1
        return total / number
    delays = map(get_delays, stations)
    def do_sum(x, y):
        return x + y
    num_stations = len(stations)
    avg_delay = reduce(do_sum, delays) / num_stations
    datum = Delays(amount=avg_delay)
    datum.save()

@shared_task
def send_delays():
    all_data = serializers.serialize('json', Delays.objects.all(), fields=('amount', 'time'))    
    async_to_sync(channel_layer.group_send)('trains', {'type': 'send_trains', 'text': str(all_data)})
