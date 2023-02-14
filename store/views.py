from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    all_products = Product.objects.all()
    special_prod = Product.objects.filter(is_special=True)

    context = {
    'all_products':all_products,
    'special_prod':special_prod
    }
    return render(request, 'store/home.html', context)
#
def products(request):
    products = Product.objects.filter()

    context = {
    'products':products,
    }
    print('PRODUCTS: ', products)
    return render(request, 'store/products.html', context)

def category(request, slug):

    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)

    context = {
    'category':category,
    'products':products,
    }
    return render(request, 'store/category.html', context)
#
def single_product(request, slug):
    pass
#     product = get_object_or_404(Product, slug=slug)
#     product_category = product.category
#     related_products = Product.objects.exclude(slug=slug)
#
#     context = {
#     'product':product,
#     'related_products':related_products
#     }
#     return render(request, 'store/single_product.html', context)

@login_required(login_url='user:login')
def add_product(request):

    if request.POST.get('action') == 'post':

        product_id = request.POST.get('productid')
        print('TYPE: ',type(product_id))

        product = get_object_or_404(Product, id=product_id)

        order, created = Order.objects.get_or_create(
        user=request.user,
        )
        order.save()

        orderitem, created = Orderitem.objects.get_or_create(
        product=product,
        order=order,
        )
        orderitem.save()

        return JsonResponse({'total_items': order.total_items })
