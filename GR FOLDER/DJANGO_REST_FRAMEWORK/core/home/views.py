from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.models import Person
from home.serializers import PeopleSerializer, LoginSerializer, RegisterSerializer
from rest_framework import viewsets
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class LoginAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response({'status':False,
                             'message' : serializer.errors
                             },status.HTTP_400_BAD_REQUEST)
        
        print(serializer.data)
        user = authenticate(username = serializer.data['username']
                            , password = serializer.data['password'])
        print(user)
        
        if not user:
            return Response({
                'status' :False,
                'message'  : 'invalid credentials'
            }, status.HTTP_400_BAD_REQUEST)
        
        
        token, _ = Token.objects.get_or_create(user=user)
        print(token)
        return  Response({'status': True, 
                          'message': 'user login',
                          'token' : str(token) 
                          },status.HTTP_201_CREATED)
 

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({'status':False,'message' : serializer.errors},status.HTTP_400_BAD_REQUEST)
        
        serializer.save()

        return Response({'status': True, 'message': 'user created'},status.HTTP_201_CREATED)




@api_view(['GET','POST','PUT'])
def index(request):
    courses ={
            'course_name':'Python',
            'learn' :['Flask','Django', 'Tornado','FastApi'],
            'course_provider': 'Scaler'
        }

    if request.method =='GET':
        print('YOU HIT A GET METHOD')
        return Response(courses)
    elif request.method == 'POST':
        print('YOU HIT A POST METHOD')
        return Response(courses)
    elif request.method == 'PUT':
         print('YOU HIT A PUT METHOD')
         return Response(courses)
    

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
    
    if serializer.is_valid():
        data = serializer.data
        print(data)
        return Response({'message': 'success'}) 
    return Response(serializer.errors)

#APIVIEW METHOD
class PersonAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        objs = Person.objects.filter(color__isnull = False)
        serializer =PeopleSerializer(objs,many = True)
        return Response(serializer.data)      

    def post(self, request):
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def put(self, request):
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.errors)
    
    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message' : 'person deleted'})


#DECORATOR METHOD
@api_view(['GET', 'POST', 'PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.filter(color__isnull = False)
        serializer =PeopleSerializer(objs,many = True)
        serializer_context = {
            'request' : (request),
        }
        context = serializer_context
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message' : 'person deleted'})

#CRUD METHOD
class PeopleViewSet(viewsets.ModelViewSet):
    
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()
    #list method
    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith=search)  # case-insensitive lookup

        serializer = PeopleSerializer(queryset, many=True)
        return Response({'status': 200, 'data': serializer.data},status=status.HTTP_204_NO_CONTENT)
    


    

