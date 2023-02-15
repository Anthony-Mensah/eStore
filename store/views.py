from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    all_products = Product.objects.all()
    special_prod = Product.objects.filter(is_special=True)
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(
        user=request.user
        )
        order.save()

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


@login_required(login_url='user:login')
def add_product(request):

    if request.POST.get('action') == 'post':

        product_id = request.POST.get('productid')
        print('TYPE: ',type(product_id))

        product = get_object_or_404(Product, id=product_id)

        order = get_object_or_404(Order, user=request.user)
        order.save()

        orderitem, created = Orderitem.objects.get_or_create(
        product=product,
        order=order,
        )
        orderitem.save()

        return JsonResponse({'total_items': order.total_items })

@login_required(login_url='user:login')
def cart(request):

    order = get_object_or_404(Order, user=request.user)
    orderitems = order.orderitem_set.all()

    context = {
    'order':order,
    'orderitems':orderitems
    }
    return render(request, 'store/cart.html', context)

def update_cart(request):

    if request.POST.get('type') == 'post':
        action = request.POST.get('action')
        productid = request.POST.get('productid')

        product = get_object_or_404(Product, id=productid)
        orderitem = get_object_or_404(Orderitem, product=product)
        order = get_object_or_404(Order, user=request.user)
        delete = False

        if action == 'add':
            orderitem.quantity += 1
        elif action == 'remove':
            orderitem.quantity -= 1

        orderitem.save()

        if orderitem.quantity < 1:
            orderitem.delete()
            delete = True

        print("Delete: ", delete)

        return JsonResponse({'quantity':orderitem.quantity,
        'subtotal':orderitem.subtotal,
        'cost':order.cost,
        'total_items':order.total_items,
        'delete':delete,
        })
