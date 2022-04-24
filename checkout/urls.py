from django.urls import path
from . import views


# url path to the home page
urlpatterns = [
    path('<int:pk>/', views.checkout, name='checkout'),
    path('checkout_success/<membership_number>', views.checkout_success, name='checkout_success'),
]
