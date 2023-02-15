from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('add-product/', views.add_product, name='add_product'),
    path('cart/',views.cart, name='cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
]
