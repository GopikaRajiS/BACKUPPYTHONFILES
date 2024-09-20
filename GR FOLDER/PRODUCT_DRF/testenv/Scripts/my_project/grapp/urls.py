from django.urls import path,include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('',index, name='index'),
    path('products/', products_list,name='product_list'),
    path('product/<int:pk>/',product_detail, name='product_detail'),
    path('example/', ExampleAPIView.as_view(), name='example_api'),
    path('home/', Home.as_view(), name='home'),
    # path('create/', views.create_resource, name='create_resource'),
    # path('update/<int:pk>/', views.update_resource, name='update_resource'),
    # path('delete/<int:pk>/', views.delete_resource, name='delete_resource'),
]