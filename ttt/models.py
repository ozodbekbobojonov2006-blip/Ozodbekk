from django.db import models
from Blog.models import User, Tag
# Create your models here.

Product_Type=(
     ('DONA', 'donali'),
     ('LITR', 'litr'),
     ('KG', 'kg')
)
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    def str(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def str(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()#12000
    product_type = models.CharField(max_length=100, choices=Product_Type, default="DONA")
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    shelf_life=models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def str(self):
        return self.name


class Order(models.Model):
    order_number = models.CharField(max_length=100)
    qty_products = models.IntegerField()
    qty_items = models.IntegerField()
    amount = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    # total_price = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def total_price(self):
        return self.quantity * self.product.price


