from django.urls import path
from .views import *

urlpatterns = [
    path('index',index, name='grapp_index')
]