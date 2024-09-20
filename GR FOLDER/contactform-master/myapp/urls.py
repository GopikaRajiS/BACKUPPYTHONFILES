# myapp/urls.py

from django.urls import path
from .views import index, get_messages


urlpatterns = [
    path('', index, name="index"),
    path('api/message', get_messages, name="get_messages"),
]
