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