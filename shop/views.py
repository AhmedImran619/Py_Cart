from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product


def index(request):
    products = list(Product.objects.all())
    output = ''
    for prod in products:
        output = output+prod.name+','

    return render(request, 'shop/index.html', context={'output':output})


def cart(request):
    return HttpResponse('Cart Page')


def categories(request):
    return HttpResponse('Categories Page')


def search():
    return HttpResponse('Search Page')


def about():
    return HttpResponse('About Page')


# ------------------------------------------------

def product_list():
    return HttpResponse('Product List Page')


def product_detail():
    return HttpResponse('Product Detail Page')


# ------------------------------------------------

def login():
    return HttpResponse('Login Page')


def register():
    return HttpResponse('Register Page')


# ------------------------------------------------

def account():
    return HttpResponse('Account Page')


def account_detail():
    return HttpResponse('Account Detail Page')


def favorites():
    return HttpResponse('Favorites Page')


def orders():
    return HttpResponse('Order Page')


def order_detail():
    return HttpResponse('Order Detail Page')
