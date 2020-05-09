from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html', {})


def mostafa(request):
    return render(request, 'mostafa.html', {})

def samara(request):
    return render(request, 'samara.html', {})


def mony(request):
    return render(request, 'mony.html', {})

def fun2(request):
    return HttpResponse("MONY YA MONY ")

def fun3(request):
    return render(request,"page1.html",{})


def fun4(request):
    return render(request,"page2.html",{})
