from django.shortcuts import render, HttpResponse, redirect
from . import models


def index(request):
    data = models.company.objects.all()
    return render(request, 'user.html', {'d': data})


def form_company(request):
    return render(request, 'form.html', {})


def insert(request):
    name = request.POST['fname']
    mail = request.POST['email']
    age = request.POST['age']
    new = models.company()
    new.fullname = name
    new.email = mail
    new.age = age
    # new = models.company(fullname=name,email=mail,age=age,birthday=birth)
    # new = models.company(fullname=request.POST['fname'],email=request.POST['email'],age=request.POST['age'],birthday=request.POST['birthday'])
    new.save()
    return redirect('/')


def delete(request, id):
    old = models.company(id=id)
    old.delete()
    return redirect('/')


def update(request, id):
    #   data = models.company.object.filter(id=id)
    # data = models.company.object.order_by('age') order by age
    # data=models.company.object.filter(fullname__in=['yaro','mostafa'])
    # data=models.company.object.filter(age__in=[35,0])
    # data=models.company.object.filter(id=8,fullname='mostafa') end
    # data=models.company.object.filter(age__gte=30) age grater than or eqle 30
    # data=models.company.object.filter(age__lte=30) age <= 30
    # print('the type is' + str(data))
    return render(request, 'update.html', {'id_company': id})


def backend_up(request, id):
    old = models.company(id=id, fullname=request.POST['fname'], email=request.POST['email'], age=request.POST['age'])
    old.save()
    return redirect('/')