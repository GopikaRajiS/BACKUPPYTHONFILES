from django.shortcuts import render
from django.http import HttpResponse

from studentapp.form import student


# Create your views here.
def index1(request):
    student = studentForm()
    return render(request,"appstudent/index.html",{'form':student})

def index2(request):
    stu = stuForm()
    return render(request,"appstudent/index2.html",{'form':stu})



def index(request):
    return HttpResponse("WE ARE CREATING A STUDENT APP BY USING DJANGO FWORKS")