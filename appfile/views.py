from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'home.html',{'name' :'james'})

def frontpage(request):
    return render(request, 'frontpage.html')

def disp(request):
    disp_task = request.GET['task1']
    disp_desc=request.GET['desc1']
    return render(request, 'display.html',{'task' : disp_task})