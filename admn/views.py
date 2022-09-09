from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from admn.forms import newuser
from datam.models import todo


def admin(request):
    if request.COOKIES.get("admin-ID") and request.COOKIES.get("admin-password"):
        if request.session['admin-ID'] and request.session['admin-password']:
            Cname = request.COOKIES.get('admin-ID')
            Cpassw = request.COOKIES.get('admin-password')
            Sname = request.session['admin-ID']
            Spassw = request.session['admin-password']
            if Cname == Sname and Cpassw == Spassw:
                return redirect('admin/home')
            else:
                return render(request, 'admin-form.html', {'ttl': "Admin-Form"})
        else:
            return render(request, 'admin-form.html', {'ttl': "Admin-Form"})
    else:
        return render(request, 'admin-form.html', {'ttl': "Admin-Form"})


def login(request):
    if request.method == 'POST':
        if request.POST['adminid'] and request.POST['AdminPassword'] :
            uname = request.POST['adminid']
            password = request.POST['AdminPassword']
            usr = auth.authenticate(username=uname,password=password)
            istaf = User.objects.get(username=uname)
            if usr and istaf.is_staff==True:
                auth.login(request,usr)
                res = redirect('admin/home')
                res.set_cookie('admin-ID', uname)
                res.set_cookie('admin-password', password)
                request.session['admin-ID'] = uname
                request.session['admin-password'] = password
                return res

            else:
                messages.error(request,'Invalid credentials or Youare not an admin')
                return redirect('/admin')
        else:
            messages.error(request, 'you cannot submit without credentials filled !')
            return redirect('/admin')
    else:
        return redirect('/admin')

@never_cache
def adminhome(request):
    if request.COOKIES.get('admin-ID') and request.COOKIES.get('admin-password'):
        Cname = request.COOKIES.get('admin-ID')
        Cpassw = request.COOKIES.get('admin-password')
        Sname = request.session['admin-ID']
        Spassw = request.session['admin-password']
        usr = auth.authenticate(username=Cname, password=Cpassw,is_staff="true")
        if usr:
            if Cname == Sname and Cpassw == Spassw:
                users = User.objects.filter()
                form = newuser()
                return render(request,'admin-home.html',{"name":Cname,'users':users,'form':form})

            else:
                return redirect('/admin')
        else:
            return redirect('/admin')
    else:
        return redirect('/admin')


def adout(request):
    del request.session
    res = redirect('/admin')
    res.delete_cookie("admin-ID")
    res.delete_cookie('admin-password')
    return res

@never_cache
def show(request,Usrid):
    Cname = request.COOKIES.get('admin-ID')
    users = User.objects.get(id=Usrid)
    Username = users.username
    td = todo.objects.filter(username=Username, task_status=False)
    dn = todo.objects.filter(username=Username, task_status=True)
    return render(request,'user-data.html',{'td':td, 'dn':dn,'username':Username,'name':Cname})

@never_cache
def delete(request,taskid):
    if request.method=="GET":
        usr=todo.objects.get(id=taskid)
        username=usr.username
        user= User.objects.get(username=username)
        usrid=user.id
        todo.objects.get(id=taskid).delete()
        return redirect('show/'+str(usrid))

@never_cache
def done(request, taskid):
    if request.method=='GET':
        usr = todo.objects.get(id=taskid)
        username = usr.username
        user = User.objects.get(username=username)
        usrid = user.id
        task=todo.objects.get(id=taskid)
        task.task_status=True
        task.save()
        return redirect('show/'+str(usrid))



def adduser(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            uname = request.POST['username']
            passw = request.POST['password']
            if request.POST['is_staff']:
                staf = True
            else:
                staf = False
            usr = User.objects.create_user(username=uname, password=passw,is_staff=staf)
            usr.save()
            print("user sign inned successfully")
            return redirect('/admin')
        else:
            messages.error(request, 'you cannot submit without credentials filled !')
            return redirect('/admin')
    else:
        return redirect('/admin')


def deleteuser(request,userid):
    if request.method == 'GET':
        User.objects.get(id=userid).delete()
        return redirect('/admin')