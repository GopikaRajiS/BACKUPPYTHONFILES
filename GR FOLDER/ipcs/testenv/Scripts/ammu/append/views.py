from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from .models import Lmodel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
def index(request):
    return HttpResponse("Hii Created a view")

def my_view(request):
    if request.method=="GET":
        return HttpResponse('result')
    
class MyView(View):
    def get(self,request):
        return HttpResponse('result')

class Create(CreateView):
    model=Lmodel
    fields=['title','description']
    template_name='append/createmodelmodel_form.html'
    context_object_name='data'
    success_url="/"

class LmodelListView(ListView):
    model=Lmodel
    template_name='append/listmodel_list.html'
    context_object_name='data'

class DetailView(DetailView):
    model=Lmodel
    template_name ='append/detailmodel_detail.html'
    context_object_name='data'

class UpdateView(UpdateView):
    model=Lmodel
    fields=[
        "title",
        "description"
    ]
    template_name='append/updatemodel_form.html'
    context_object_name='data'
    success_url="/"

class DeleteView(DeleteView):
    model=Lmodel
    success_url="/"
    template_name="append/deletemodel_confirm_delete.html"