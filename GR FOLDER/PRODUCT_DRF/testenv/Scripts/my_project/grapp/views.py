from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Product
from django.forms.models import model_to_dict
import json

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
#JWT AUTH
from rest_framework.permissions import IsAuthenticated #, AllowAny #allowany - to allow unauthorized users to view
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.decorators import api_view, permission_classes


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

# Create your views here.
# @csrf_exempt
# def create_resource(request):
#     if request.method == 'POST':
#         data = request.POST
#         new_resource = Product.objects.create(data)
#         return JsonResponse({'message': 'Resource created successfully'},status=201)
#     else:
#         return JsonResponse({'error':'Method not allowed'},status=405)
#
# @csrf_exempt
# def update_resource(request,resource_id):
#     if request.method == 'PUT':
#         try:
#             resource = Product.objects.get(id=resource_id)
#             for key, value in request.POST.items():
#                 setattr(resource,key,value)
#             resource.save()
#             return JsonResponse({'message':'Resource updated successfully'})
#         except Product.DoesNotExist:
#             return JsonResponse({'error': 'Resource not found'},status=404)
#     else:
#         return JsonResponse({'error':'Resource not found'},status=405)
#
#
# @csrf_exempt
# def delete_resource(request,resource_id):
#     if request.method == 'DELETE':
#         try:
#             resource = Product.objects.get(id=resource_id)
#             resource.delete()
#             return JsonResponse({'message': 'Resource deleted successfully'})
#         except Product.DoesNotExist:
#             return JsonResponse({'error': 'Resource not Found'},status=404)
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)




class ExampleAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Example API",
        responses={200: openapi.Response("Example response")}
    )
    def get(self, request):
        return Response({"message": "Hello, world!"})



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
@csrf_exempt
def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = {'products':[model_to_dict(product)for product in products]}
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            product = Product.objects.create(name=data["name"], description=data["description"], price= data["price"])
            return JsonResponse({'success':'Product created successfully','product':model_to_dict(product)},status=201)
        except KeyError:
            return JsonResponse({'error':'Missing required Fields'},status=400)

@csrf_exempt
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    if request.method == 'GET':
        return JsonResponse({'product': model_to_dict(product)})

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            product.name = data.get('name', product.name)
            product.description = data.get('description', product.description)
            product.price = data.get('price', product.price)
            product.save()
            return JsonResponse({'success': 'Product updated successfully', 'product': model_to_dict(product)})
        except KeyError:
            return JsonResponse({'error': 'Missing required fields'}, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'success': 'Product deleted successfully'}, status=204)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)



# def index(request):
#     return HttpResponse("DJANGOREST API")