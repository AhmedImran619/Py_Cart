from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def index(request):
    products = Product.objects.all()

    products_per_slide = 4

    n = len(products)
    no_of_slides = (n // 4) + ceil((n / 4) - (n // 4))

    context = {
        'products': products,
        'no_of_slides': no_of_slides,
        'products_per_slide': range(products_per_slide),
        'range': range(no_of_slides)
    }

    return render(request, 'shop/index.html', context=context)


def cart(request):
    return HttpResponse('Cart Page')


def categories(request):
    return HttpResponse('Categories Page')


def search(request):
    return HttpResponse('Search Page')


def about(request):
    return HttpResponse('About Page')


# ------------------------------------------------

def product_list(request):
    return HttpResponse('Product List Page')


def product_detail(request):
    return HttpResponse('Product Detail Page')


# ------------------------------------------------

def login(request):
    return HttpResponse('Login Page')


def register(request):
    return HttpResponse('Register Page')


# ------------------------------------------------

def account(request):
    return HttpResponse('Account Page')


def account_detail(request):
    return HttpResponse('Account Detail Page')


def favorites(request):
    return HttpResponse('Favorites Page')


def orders(request):
    return HttpResponse('Order Page')


def order_detail(request):
    return HttpResponse('Order Detail Page')
