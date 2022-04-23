from django.urls import path
from . import views


# url path to the home page
urlpatterns = [
    path('', views.index, name='home'),
    path('membership', views.membership, name='membership'),
    path('<product_id>', views.membership_detail, name='membership_detail'),
]
