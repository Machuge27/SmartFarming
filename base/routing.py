#routing.py

from django.urls import re_path
from .consumer import ChatConsumer
from .consumer import ChatDm
from channels.routing import ProtocolTypeRouter,URLRouter

websockets_urlpatterns=[
    re_path(r'ws/Chatts/$',ChatConsumer.as_asgi()),
    re_path(r'ws/dm/$',ChatDm.as_asgi())
]