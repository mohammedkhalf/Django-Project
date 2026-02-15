from django.shortcuts import render
from .models import Product

# create index products page
def index(request):
    # print("data", Product.objects.get(id=2))
    # breakpoint()
    x = {'pro':Product.objects.all().filter(price=12)}
    return render ( request,'products/index.html',x)

# create show product
def show (request):
    return render(request,'products/show.html')