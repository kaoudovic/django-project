from django.shortcuts import render, HttpResponse, redirect
from . import models
from .forms import staff_form
from .models import staff
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    return HttpResponse('hello')


def register(request):
    form = staff_form(request.POST or None)
    obj = staff()
    if form.is_valid():
        if not request.POST['birthday']:
            obj.birthday = "2020-7-5"
        else:
            obj.birthday = form.cleaned_data['birthday']
        if not request.POST['email']:
            obj.email = "default@gmail.com"
        else:
            obj.email = form.cleaned_data['email']
        obj.name = form.cleaned_data['name']
        obj.age = form.cleaned_data['age']
        #  obj.department=form.cleaned_data['department']
        # obj.code=form.cleaned_data['code']
        print('Name is :', form.cleaned_data['name'])
        print('Email is :', form.cleaned_data['email'])
        print('Age is :', form.cleaned_data['age'])
        print('Birthday is :', form.cleaned_data['birthday'])
        obj.save()
        return redirect('/c3')
    return render(request, 'staff_reg.html', {'f': form})


############################################3
# register
########################


def registration(request):
    return render(request, 'registeration.html', {})


def register_backend(request):
    try:
        user = User.objects.create_user(request.POST['uname'], request.POST['email'], request.POST['pass'])
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.save()
        return redirect('/c3')
    except:
        return redirect("/c3/register")
        # return HttpResponse("user is exsist")


#################################
# login
#################################


def log(request):
    return render(request, 'login.html', {})


def profile(request,username):
    return render(request, 'profile.html', {})


def login_backend(request):
    username = request.POST['uname']
    password = request.POST['pass']
    result = authenticate(username=username, password=password)
    if result is not None:
        login(request, result)
        link = '/c3/profile/' +str(result)
        return redirect(link)
        # return HttpResponse('Welcome'+' '+username)
    else:
        return HttpResponse('user not exist')


def logout_backend(request):
    logout(request)
    return HttpResponse('logged out')
