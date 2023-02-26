from django.shortcuts import render
from .models import articls

def base_hom(request):
    news=articls.objects.all()
    return render(request,'blog/lusa.html',{'news':news})