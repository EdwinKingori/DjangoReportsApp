from django.shortcuts import render
from .models import Sale

# Create your views here.


def home_view(request):
    return render(request, 'sales/main.html', {

    })
