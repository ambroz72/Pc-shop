from django.shortcuts import render
from pcapp.models import Product

def allproduct(request,c_slug=None):
    c_page=None
    products=None
    if c_slug!=None:
        c_page=get_or_404(Category,slug=c_slug)
        products=Product.objects.all().filter(category=c_page,available=True)
    else:
        products=Product.objects.all().filter(available=True)
    return render(request,'category.html',{'category':c_page,'products':products})   