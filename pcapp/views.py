from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def allproduct(request,c_slug=None):
    c_page=None
    products=None
    if c_slug!=None:
        c_page=get_or_404(Category,slug=c_slug)
        products=Product.objects.all().filter(category=c_page,available=True)
    else:
        products=Product.objects.all().filter(available=True)
    return render(request,'castegory.html',{'category':c_page,'products':products})