from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<p>start</p>')

def about(request):
    return HttpResponse('<p>rot</p>')