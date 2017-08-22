from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect

from .models import Product

from .forms import ProductForm

from django.utils import timezone


now = timezone.now()

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product_name = request.POST.get('product_name')
            description = request.POST.get('description')
            product_obj = Product(product_name=product_name, product_description=description, published=now, last_modified=now)
            product_obj.save()
            return HttpResponseRedirect('/rgapp/')

    else:
        form = ProductForm()

    return render(request, 'addproduct.html', {'form':form})