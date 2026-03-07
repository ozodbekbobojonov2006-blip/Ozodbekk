from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255)
    balance = models.IntegerField(default=0)
    rating = models.FloatField(default=5.0)
    joined_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

class Item(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_day = models.IntegerField()
    image_main = models.ImageField(upload_to='items/')
    city = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

class Rental(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    renter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.IntegerField()
    is_confirmed = models.BooleanField(default=False)

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    comment = models.TextField()

class Wishlist(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

class Transaction(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)