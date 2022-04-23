from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings


# Create your views here.

def checkout(request):
    """ A view to index page """

    return render(request, 'checkout/checkout.html')
