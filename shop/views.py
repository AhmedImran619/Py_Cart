from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    PRODUCTS_COUNT_FOR_ACTIVE_SLIDE = int(5)
    products = Product.objects.all()

    tab_indicator_count = len(products) / PRODUCTS_COUNT_FOR_ACTIVE_SLIDE

    context = {
        'products': products,
        # 'tab_indicator_count': tab_indicator_count,
        # 'items_range': range(PRODUCTS_COUNT_FOR_SLIDER),
        # 'products_count': PRODUCTS_COUNT_FOR_SLIDER
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
