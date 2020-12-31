from django.shortcuts import render,redirect
from product.models import Product
from .forms import *
# Create your views here.
def add_product(request):
    form = ProductForm(request.POST or None )
    if form.is_valid():
        form.save()
        return redirect('view_product')
    else:
        form = ProductForm()
    return render(request,'product/add_product.html',{'form':form})

def view_product(request):
    product = Product.objects.all()
    qty = Product.objects.all().count()
    context={'qty':qty,'product':product}
    return render(request, 'product/view_product.html', context)

def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect('view_product')
    return render(request,'product/update.html',{'product':product})

def delete(request,id):
    if request.method == 'GET':
        product = Product.objects.filter(id=id)
        product.delete()
    return redirect("view_product")
