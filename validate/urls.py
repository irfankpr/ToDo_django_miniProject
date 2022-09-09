
from django.urls import path, include


from validate import views

urlpatterns = [
    path('', views.index,name='index'),
    path('signin',views.signin),
    path('login', views.login),
    path('home',views.home,name='home'),
    path('logout',views.logout),
]
