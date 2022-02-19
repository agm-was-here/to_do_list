from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('frontpage',views.frontpage,name='frontpage'),
    # path('disp', views.disp, name='disp'),
    path('taskdisp', views.taskdisp, name='taskdisp'),
    path()
]