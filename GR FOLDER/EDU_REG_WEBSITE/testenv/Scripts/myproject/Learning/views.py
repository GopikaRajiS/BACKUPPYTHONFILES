from django.shortcuts import render
from django.http import HttpResponse
from .models import  Register2


# Create your views here.
def index(request):
    return HttpResponse("<b>Hi lets create a education learning website and let us learn how to register in that page<b>")

def home(request):
    return render(request,'home.html')

def register(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    address = request.POST.get('address')
    email = request.POST.get('email')
    z = Register2(name=name,password=password,address=address,email=email)
    z.save()
    return render(request, "output.html",{'Name':name,'Password':password,'Address':address,'Email':email})

def main(request):
    return render(request,'main.html')