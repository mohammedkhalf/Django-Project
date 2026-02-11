from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):
    x = {'name':'ahmed' , 'age':'45 years'}
    return render(request,'pages/index.html',x)

def about(request):
    return HttpResponse('about page')