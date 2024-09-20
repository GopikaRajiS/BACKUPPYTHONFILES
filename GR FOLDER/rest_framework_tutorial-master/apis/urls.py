# basic URL Configurations
# from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views

# from . import views
# from .swagger import schema_view

# define the router
router = routers.DefaultRouter()

from django.urls import include, path
from rest_framework import routers
from . import views

# Import drf-yasg for Swagger documentation
from rest_framework import permissions
# from drf_yasg.views import schema_view
from drf_yasg import openapi

# Define the router
router = routers.DefaultRouter()


# Define the schema view for Swagger
def schema_view(param, public, permission_classes):
    pass


schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# define the router path and viewset to be used
# router.register(r'geeks', GeeksViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    path('home/', views.ApiOverview, name='home'),
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view_items'),
    path('update/<int:pk>/', views.update_items, name='update-items'),
    path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),

    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
