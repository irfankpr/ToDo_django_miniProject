# datam . urls

from datam import views
from django.contrib import admin
from django.shortcuts import render
from django.urls import path


urlpatterns = [
    path('', views.addtask),
    path('delete/<int:taskid>',views.delete,name='delete'),
    path('done/<int:taskid>',views.done,name='done'),
    path('remove/<int:taskid>',views.delete, name='remove')
]
