from django.urls import path, include
from admn import views

urlpatterns = [
    path('admin', views.admin),
    path('admin-login',views.login),
    path('admin/home',views.adminhome),
    path('admin/adout',views.adout),
    path('show/<int:Usrid>',views.show,name='show'),
    path('admin-remove/show/<int:Usrid>',views.show,name='show'),
    path('admin-done/show/<int:Usrid>',views.show,name='show'),
    path('admin-delete/show/<int:Usrid>',views.show,name='show'),
    path('admin-delete/<int:taskid>',views.delete,name='admin-delete'),
    path('admin-done/<int:taskid>',views.done,name='admin-done'),
    path('admin-remove/<int:taskid>',views.delete, name='admin-remove'),
    path('admin/newuser', views.adduser),
    path('delete-user/<int:userid>', views.deleteuser, name='delete-user'),
]
