from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import given_task,TodoListItem

def index(request):
    return render(request, 'home.html',)

def frontpage(request):
    ll_items = TodoListItem.objects.all()
    return render(request, 'frontpage.html',{'item':ll_items})

def taskdisp(request):
    list =given_task.objects.all()
    return render(request, 'taskdisp.html',{'list':list})

def todoview(request):
    x=request.GET['task1']
    new = TodoListItem(tsk=x)
    new.save()
    return HttpResponseRedirect("/appfile/frontpage")

def deleteitem(request,i):
     n = TodoListItem.objects.get(id= i)
     n.delete()
     return HttpResponseRedirect("/appfile/frontpage")