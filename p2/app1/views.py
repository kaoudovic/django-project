from django.shortcuts import render, HttpResponse, redirect
from . import models


def index(request):
    return HttpResponse('hello')