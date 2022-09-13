from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
# Create your views here.


# views . validate
from django.views.decorators.cache import never_cache

from datam.forms import newtask
from datam.models import todo


def index(request):
    if request.COOKIES.get("username") and request.COOKIES.get("password"):
        if request.session['username'] and request.session['password']:
            Cname = request.COOKIES.get('username')
            Cpassw = request.COOKIES.get('password')
            Sname = request.session['username']
            Spassw = request.session['password']
            if Cname == Sname and Cpassw == Spassw:
                return redirect('/home')
            else:
                return  render(request,"user-form.html")
        else:
            return  render(request,"user-form.html")
    else:
        return  render(request,"user-form.html")



# signup module
def signin(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password1'] and request.POST['password2']:
            uname = request.POST['username']
            pass1 = request.POST['password1']
            pass2 = request.POST['password2']
            if pass2 == pass1:
                usr = User.objects.create_user(username=uname, password=pass1)
                usr.save()
                print("user sign inned successfully")
                auth.login(request, usr)
                res = redirect('/')
                res.set_cookie('username',uname)
                res.set_cookie('password', pass1)
                request.session['username'] = uname
                request.session['password'] = pass1
                return res
            else:
                print("password confirmation failed")
                messages.error(request, 'Password confirmation failed ')
                return redirect('/')
        else:
            messages.error(request, 'you cannot submit without credentials filled !')
            return redirect('/')
    else:
        return redirect('/')

#login module
@never_cache
def login(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password'] :
            uname = request.POST['username']
            password = request.POST['password']
            usr = auth.authenticate(username=uname,password=password)
            if usr:
                auth.login(request,usr)
                res = redirect('/')
                res.set_cookie('username', uname)
                res.set_cookie('password', password)
                request.session['username'] = uname
                request.session['password'] = password
                return res

            else:
                messages.error(request,'Invalid credentials.')
                return redirect('/')
        else:
            messages.error(request, 'you cannot submit without credentials filled !')
            return redirect('/')
    else:
        return redirect('/')
#logout module
def logout(request):
    if 'username' in request.session and 'password' in request.session:
        del request.session['username']
        del request.session['password']
    res = redirect('/')
    res.delete_cookie("username")
    res.delete_cookie('password')
    return res


@never_cache
def home(request):
    if request.COOKIES.get('username') and request.COOKIES.get('password'):
        Cname = request.COOKIES.get('username')
        Cpassw = request.COOKIES.get('password')
        Sname = request.session['username']
        Spassw = request.session['password']
        usr = auth.authenticate(username=Cname, password=Cpassw)
        if usr:
            if Cname == Sname and Cpassw == Spassw:
                form=newtask()
                td = todo.objects.filter(username=Cname,task_status=False)
                dn = todo.objects.filter(username=Cname,task_status=True)
                tdCount = todo.objects.filter(username=Cname,task_status=False).count()
                dnCount = todo.objects.filter(username=Cname,task_status=True).count
                return render(request, 'home.html', {'name': Cname, 'form':form, 'td':td ,'dn':dn, 'tdCount':tdCount, 'dnCount':dnCount,'ttl':"My-Book"})
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')

def userForm(request):
    return  render(request,"user-form.html",{'ttl':"User-Form"})