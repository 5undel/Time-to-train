from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.


def index(request):
    """ A view to index page """

    return render(request, 'base/index.html')


def membership(request):
    """ A view to return the membership page """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'base/membership.html', context)


def membership_detail(request, product_id):
    """ A view to return the membership detail page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'base/membership_detail.html', context)
