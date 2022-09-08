from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

import datam.views
from datam import views
from validate import views

urlpatterns = [
    path('', views.index,name='index'),
    path('admin', views.admin),
    path('signin',views.signin),
    path('login', views.login),
    path('home',views.home,name='home'),
    path('logout',views.logout),
    path('newtask', include('datam.urls')),
]
