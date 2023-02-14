from django.shortcuts import render, get_object_or_404
from .models import Category, Order


def categories(request):
    return {'categories':Category.objects.all()}


def order(request):
    if request.user.is_authenticated:
        try:
            order = Order.objects.get(user=request.user)
        except:
            order = 0
        return {'order':order}
    else:
        return {'order':0}
