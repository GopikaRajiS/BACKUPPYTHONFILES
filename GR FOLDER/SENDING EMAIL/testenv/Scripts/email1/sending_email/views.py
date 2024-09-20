from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def index(request,):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            'Contact Form',#title
            message,#message
            'settings.EMAIL_HOST_USER',#sender
            ['juswin345@gmail.com'],#receiver
            fail_silently=False)
        return render(request,'index.html')

