from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Messages
import json

# Create your views here.

def index(request):
    return HttpResponse(" My App works")

def get_messages(request):
    objects = Messages.objects.all()

    result = []

    for obj in objects:
        result.append({"name": obj.name, "email": obj.email,
        "mobile": obj.mobile, "messages":obj.message,
        "created_at": str(obj.created_at)})
   
    return JsonResponse(result,safe=False)