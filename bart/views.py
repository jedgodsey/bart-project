from django.shortcuts import render
import requests
# import json

def index(request):
    url = 'http://api.icndb.com/jokes/random/'
    response = requests.get(url).json()
    train = response['value']['joke']
    return render(request, 'index.html', context={'text': train})
