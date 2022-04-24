from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import MembershipForm
from base.models import Product
from .models import CreateMembership, MembershipNumber

import stripe
# Create your views here.

def checkout(request, pk):
    """ A view to complite payment """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'order_total': product.price,
            'grand_total': product.price,
        }
        print(form_data)
        order_form = MembershipForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()

        request.session['save_info'] = 'save-info' in request.POST
        return redirect(reverse('checkout_success', args=[order.membership_number]))
    else:
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
        amount=int(product.price * 100),
        currency=settings.STRIPE_CURRENCY,
        )
        order_form = MembershipForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'product': product,
        }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, membership_number):
    """ A view to Show payment success page """

    save_info = request.session.get('save_info')
    order = get_object_or_404(
        CreateMembership, membership_number=membership_number)


    if save_info:
        profile_data = {
            'phone_number': order.phone_number,
            'country': order.country,
            'postcode': order.postcode,
            'town_or_city': order.town_or_city,
            'street_address1': order.street_address1,
            'street_address2': order.street_address2,
        }

    messages.success(request, f'Membership successfully processed! \
        Your membership number is {membership_number}. A confirmation \
        email will be sent to {order.email}')

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)