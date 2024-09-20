from django.urls import path
from .views import *
#from .views import FormView


urlpatterns=[
    path('', index, name='appcrud_index'),
    #cmt:use "/l/" to view the page
    path('l/', LmodelListView.as_view(), name='appcrud/listmodel_list'),
    #cmt:use "/1/" to view the page, the num denotes the datas present in the table
    path('<pk>/', DetailView.as_view(), name='appcrud/detailmodel_detail'),
    #cmt:use "/create/" to view the createmodel page
    path('create/', Create.as_view(), name='appcrud/createmodelmodel_form'),
    #cmt:use "/1/update" to view the updatemodel page
    path('<pk>/update/', UpdateView.as_view(), name='appcrud/updatemodel_form'),
    #cmt:use "/give nummber/delete" to delete the data in the table using deletemodel
    path('<pk>/delete/', DeleteView.as_view(), name='appcrud/deletemodel_confirm_delete'),
]
