from django.urls import path
from .views import *
from append.views import MyView


urlpatterns=[
    path('',index,name='append_index'),
    path('ml/',my_view),
    path('about/',MyView.as_view()),
    path('create/',Create.as_view(),name="append/createmodelmodel_form"),

    path('l/',LmodelListView.as_view(),name='append/listmodel_list'),

    path('<pk>/',DetailView.as_view(),name='append/detailmodel_detail'),
    path('<pk>/update/',UpdateView.as_view(),name='append/updatemodel_form'),
    path('<pk>/delete/',DeleteView.as_view(),name='append/deletemodel_confirm_delete'),
                  
]