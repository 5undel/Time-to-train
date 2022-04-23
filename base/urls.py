from django.urls import path
from . import views


# url path to the home page
urlpatterns = [
    path('', views.index, name='home'),
]
