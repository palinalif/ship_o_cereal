from django.shortcuts import render, get_object_or_404, redirect
from products.models import *
from products.forms.createProduct import ProductForm
from error.views import *

# Create your views here.


def getCereals():
    return Product.objects.all()


def product(request, id):
    # TODO: make id check and if invalid goto 404 page
    return render(request, 'products/index.html', {
        'cereal': get_object_or_404(Product, pk=id)
    })


def createProduct(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(data=request.POST)
            if form.is_valid():
                cereal = form.save()
                cerealImage = ProductImage(image=request.POST['image'], product=cereal)
                cerealImage.save()
                return redirect('catalog-page')
        else:
            form = ProductForm()
        return render(request, 'products/create.html', {
            'form': form
        })
    return error_403_view(request, None)


def deleteProduct(request, id):
    if request.user.is_superuser:
        cereal = get_object_or_404(Product, pk = id)
        cereal.delete()
        return redirect('catalog-page')
    return error_403_view(request, None)


def updateProduct(request, id):
    if request.user.is_superuser:
        instance = get_object_or_404(Product, pk = id)
        if request.method == 'POST':
            form = ProductForm(data=request.POST, instance=instance)
            if form.is_valid():
                form.image = request.POST['image']
                form.save()
                return redirect('product-index', id=id)
        else:
            form = ProductForm(instance=instance, initial={
                'image': ProductImage.objects.filter(product=instance).first().image
            })
        return render(request, 'products/update.html', {
            'form': form,
            'id': id
        })
    return error_403_view(request, None)