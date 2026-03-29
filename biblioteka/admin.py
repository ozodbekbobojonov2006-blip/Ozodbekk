from django.contrib import admin
from .models import (
    Customer, Book, OrderRental,
    OrderItem, Tariff, TariffCustomer
)

# Buyurtma ichida kitoblarni (OrderItem) ko'rsatish uchun Inline
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1 # Bo'sh qatorlar soni
    readonly_fields = ('price_at_order',) # Bu maydon avtomatik to'ladi, o'zgartirib bo'lmaydi

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'customer_type', 'coupon_code', 'phone')
    list_filter = ('customer_type',)
    search_fields = ('full_name', 'phone', 'coupon_code')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author', 'price', 'stock')
    search_fields = ('book_name', 'author', 'isbn')
    list_editable = ('price', 'stock') # Admin ro'yxatidan turib o'zgartirish imkoniyati

@admin.register(OrderRental)
class OrderRentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'customer', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'customer__full_name')
    list_editable = ('status',)
    inlines = [OrderItemInline] # Buyurtma ichida kitoblarni boshqarish

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('tariff_name', 'tariff_price', 'duration_days')

@admin.register(TariffCustomer)
class TariffCustomerAdmin(admin.ModelAdmin):
    list_display = ('customer', 'tariff', 'start_date', 'is_active')
    list_filter = ('is_active', 'tariff')
    search_fields = ('customer__full_name',)

# Agar OrderItem-ni alohida ham ko'rmoqchi bo'lsangiz:
# admin.site.register(OrderItem)