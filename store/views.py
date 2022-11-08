from django.shortcuts import render
from django.shortcuts import render
from store.models import Product, Category

def store(request):

    products = Product.objects.all()
    return render(request, 'store/store.html', {'products': products})

def category(request, category_id):

    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(categories= category)
    return render(request, 'store/categories.html', {'category': category, 'products': products})