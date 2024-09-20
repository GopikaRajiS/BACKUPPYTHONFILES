from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello Sanjay....I created the app")
#view.py
def mypage(request):
    return render(request,
    template_name='mypage.html',
    context={'name':'sanjay',
    'address':'18,Chinnathurai,Enayam'})


