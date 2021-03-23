from django.urls import path

from .consumers import TrainsConsumer

ws_urlpatterns = [
    path('ws/trains/', TrainsConsumer.as_asgi())
]
