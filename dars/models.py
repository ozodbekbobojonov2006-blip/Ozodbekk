from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='Kategoriya',max_length=100)
    description = models.CharField(verbose_name='Tavsifi',max_length=100)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name='Nome',max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
class AttributeValue(models.Model):
    name = models.CharField(verbose_name='Nome',max_length=100)
    tag = models.CharField(verbose_name='Tavsifi',max_length=100)
    attribute = models.ForeignKey('Attribute', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.attribute.name+": "+self.name+"; "+self.product.name

class Attribute(models.Model):
    name = models.CharField(verbose_name='Nomi',max_length=100)

    def __str__(self):
        return self.name


class VendorProfile(models.Model):
    full_name = models.CharField(verbose_name='Nome',max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.full_name

   

class Shop(models.Model):
    name = models.CharField(verbose_name='Nomi',max_length=100)
    adress = models.CharField(verbose_name='Adress',max_length=100)
    phone = models.CharField(verbose_name='Telefon',max_length=100)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(verbose_name='Nomi',max_length=100)
    email = models.EmailField(verbose_name='Email',max_length=100)
    phone = models.CharField(verbose_name='Telefon',max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='mijoz'
        verbose_name_plural='mijozlar'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.customer.name if self.customer else "No customer"

    @property
    def total(self):
        if self.product:
            return self.quantity * self.product.price
        return 0
    

