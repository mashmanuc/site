from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'blog/index.html')

def about(request):
    return render(request,'blog/about.html')
def lusa(request):
    return render(request,'blog/lusa.html')