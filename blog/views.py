from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data={
        'title':'Головна сторінка',
        'velues':['Some','home','655555'],
    }
    return render(request,'blog/index.html', data)

def about(request):
    data={
        'title':'Про нас'
    }
    return render(request,'blog/about.html', data)
def lusa(request):
    data={
        'title':'Все'
    }
    return render(request,'blog/lusa.html', data)