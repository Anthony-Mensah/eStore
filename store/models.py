from django.db import models
from django.urls import reverse
from user.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=233, unique=True, null=True)

    def get_absolute_url(self):
        return reverse('store:category', args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    quantity = models.IntegerField(default=1, null=True)
    is_special = models.BooleanField(default=False, null=True)
    in_stock = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    added = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    transaction_id = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False)

    @property
    def cost(self):
        orderitems = self.orderitem_set.all()
        cost = 0
        for i in orderitems:
            cost += i.subtotal

        return cost

    @property
    def total_items(self):
        orderitems = self.orderitem_set.all()
        total = 0
        for i in orderitems:
            total += i.quantity

        return total

    # def __str__(self):
    #     return self.user + " - " + self.complete

class Orderitem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)

    @property
    def subtotal(self):
        return self.product.price * self.quantity

    # def __str__(self):
    #     return self.product
