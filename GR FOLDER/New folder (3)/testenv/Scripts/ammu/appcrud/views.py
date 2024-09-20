from django.shortcuts import render, redirect
from django.http import HttpResponse
from http.client import HTTPResponse
from multiprocessing import context

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


from .models import Lmodel

# Create your views here

#Instantiate the form
# def emp(request):
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             try:
#                 return redirect('/')
#             except:
#                 pass
#     else:
#         form = EmployeeForm()
#     return render(request,'form.html',{'form':form})

class DeleteView(DeleteView):
    # specify the model you want to use
    model = Lmodel
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/"
    template_name = "appcrud/deletemodel_confirm_delete.html"

class UpdateView(UpdateView):
    # specify the model you want to use
    model = Lmodel
    # specify the fields
    fields = [
        "title",
        "description"
    ]
    template_name = 'appcrud/updatemodel_form.html'
    context_object_name = 'data'
     # can specify success url
    # url to redirect after successfully updating details
    success_url ="/"

class Create(CreateView):
    # specify the model for create view
    model = Lmodel
    # specify the fields to be displayed
    fields = ['title', 'description']
    template_name = 'appcrud/createmodelmodel_form.html'
    context_object_name = 'data'

class DetailView(DetailView):
    # specify the model to use
    model = Lmodel
    template_name = 'appcrud/detailmodel_detail.html'
    context_object_name = 'data'

class LmodelListView(ListView):
	# specify the model for list view
    model = Lmodel
    template_name = 'appcrud/listmodel_list.html'
    context_object_name = 'data'

def  index(request):
    context ={}
    context['data'] = Lmodel.objects.all()
    return render(request, 'index.html', context)

def index(request):
    return HttpResponse('Hello we are creating crud process to create, retrive, update, delete, to listview')
