from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('product/<slug:slug>/', views.single_product, name='single_product'),
    path('add-product/', views.add_product, name='add_product'),
]
