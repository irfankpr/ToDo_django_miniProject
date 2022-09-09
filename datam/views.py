from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from datam.forms import newtask
from datam.models import todo


def addtask(request):
    Cname = request.COOKIES.get('username')
    form= newtask(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            task=form.save(commit=False)
            task.username = Cname
            task.save()
            print(Cname)
            return redirect('/')
        else:
            print('form not valid')
            messages.error(request, 'Field cannot be empty')
            return redirect('/')
    else:
        return redirect('/')


def delete(request,taskid):
    if request.method=="GET":
        todo.objects.get(id=taskid).delete()
        return redirect('/')

def done(request, taskid):
    if request.method=='GET':
        task=todo.objects.get(id=taskid)
        task.task_status=True
        task.save()
        return redirect('/')

