from django.contrib import admin
from .models import Profile, Category, Item, Rental, Review, Wishlist, FAQ, Transaction

admin.site.register([Profile, Category, Item, Rental, Review, Wishlist, FAQ, Transaction])