#routing.py

from django.urls import re_path
from .consumer import ChatConsumer
from .consumer import ChatDm
from channels.routing import ProtocolTypeRouter,URLRouter

websockets_urlpatterns=[
    re_path(r'ws/Chatts/$',ChatConsumer.as_asgi()),
    # re_path(r'ws/dm/$',ChatDm.as_asgi()),
    re_path(r'ws/dm/(?P<group_id>\w+)/$', ChatDm.as_asgi()),
]

"""
The pattern r'ws/dm/(?P<group_id>\w+)/$' is a regular expression (regex) pattern used to match URLs. Let's break it down:

r: This denotes a raw string literal in Python, which means that backslashes are treated as literal characters. It's often used with regular expressions to avoid issues with escape characters.
'ws/dm/': This part of the pattern simply matches the string literal "ws/dm/" in the URL.
(?P<group_id>\w+): This is a named capture group in the regular expression. Here's what it does:
(?P<group_id>...): This syntax defines a named capture group where group_id is the name of the group.
\w+: This part of the pattern matches one or more word characters (letters, digits, or underscores). It's used to capture the group_id from the URL.
/$: This matches the end of the URL string. The $ anchor signifies the end of the string.
So, putting it all together, the pattern r'ws/dm/(?P<group_id>\w+)/$' is designed to match WebSocket URLs that start with "ws/dm/", followed by a group_id consisting of one or more word characters, and ending with a slash ("/"). The group_id is captured and can be accessed as a parameter in the view or consumer handling the WebSocket connection.
"""