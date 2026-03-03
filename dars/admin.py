from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(AttributeValue)
admin.site.register(Attribute)
admin.site.register(VendorProfile)