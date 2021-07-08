from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('cart/', views.cart, name='CartPage'),
    path('categories/', views.categories, name='CategoriesPage'),
    path('search/', views.search, name='SearchPage'),
    path('about/', views.about, name='AboutPage'),

    path('product_list/', views.product_list, name='ProductListPage'),
    path('product_detail/', views.product_detail, name='ProductDetailPage'),

    path('login/', views.login, name='LoginPage'),
    path('register/', views.register, name='RegisterPage'),

    path('account/', views.account, name='AccountPage'),
    path('account_detail/', views.account_detail, name='AccountDetailPage'),
    path('favorites/', views.favorites, name='FavoritesPage'),
    path('orders/', views.orders, name='OrdersPage'),
    path('order_detail/', views.order_detail, name='OrderDetailPage'),
]
