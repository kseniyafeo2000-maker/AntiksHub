from django.shortcuts import render
from .models import Product

def index(request):
    # Берем только активные товары
    products = Product.objects.filter(is_active=True)
    return render(request, 'products/list.html', {'products': products})
