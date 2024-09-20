from django.urls import path
from studentapp.views import *

urlpatterns = [
    path('',index, name ='app_index'),
    path('index1/', views.index1, name='studentapp/index'),
    path('index2/', views.index2, name='studentapp/index2'),
]