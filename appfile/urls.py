from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('frontpage',views.frontpage,name='frontpage'),
    path('taskdisp', views.taskdisp, name='taskdisp'),
    path('todoview/', views.todoview),
]