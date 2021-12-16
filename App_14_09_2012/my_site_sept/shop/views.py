from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Product


def first_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'first_page.html', context)