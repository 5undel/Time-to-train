from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to return the index page """

    return render(request, 'base/index.html')