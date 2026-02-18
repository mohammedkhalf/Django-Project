from django.shortcuts import render
from .models import Product

# create index products page
def index(request):
    # print("data", Product.objects.get(id=2))
    # breakpoint()
    pro = Product.objects.all()
    x = {'pro':pro.exclude(name='test1')} 
    return render ( request,'products/index.html',x)

# create show product
def show (request):
    return render(request,'products/show.html')