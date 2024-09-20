from django.urls import path
from AmuzeApp import views
from .views import *

urlpatterns=[
    path('', views.index, name="AmuzeApp_index"),
    path('mypage', views.mypage, name='mypage'),
]

