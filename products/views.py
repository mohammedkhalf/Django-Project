from django.shortcuts import render
from .models import Product

# create index products page
def index(request):
    return render(request,'products/index.html',{'pro':Product.objects.all()})

# create show product
def show (request):
    return render(request,'products/show.html')