from django.urls import path, include
from .views import ProductPage

urlpatterns = [
    # path('shop/', ),
    path('shop/products/<slug:product>/', ProductPage, name='product_url'),
]
