from product.models import Product
from django.shortcuts import get_object_or_404, render

# Create your views here.
def products_s(request,slug):

    item = get_object_or_404(Product, slug = slug)
    
    return render(request,"sitemap.html",{'product':item})