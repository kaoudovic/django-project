from django.shortcuts import render, HttpResponse, redirect
from . import models
from .forms import staff_form
from .models import staff


def index(request):
    return HttpResponse('hello')


def register(request):
    form=staff_form(request.POST or None)
    obj =staff()
    if form.is_valid():
        obj.name=form.cleaned_data['name']
        obj.email=form.cleaned_data['email']
        obj.age=form.cleaned_data['age']
        obj.birthday=form.cleaned_data['birthday']
        obj.save()
        return redirect('/c3')
    return render(request,'staff_reg.html',{'f':form})