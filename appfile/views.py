from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import given_task

def index(request):
    return render(request, 'home.html',{'name' :'james'})

def frontpage(request):
    return render(request, 'frontpage.html')

def taskdisp(request):
    list =given_task.objects.all()
    return render(request, 'taskdisp.html',{'list':list})

# def todoappView(request):
#     return render(request, 'todolist.html')