from django.contrib import admin
from .models import Category, Tag, Product, Order, OrderItem


# ===== CATEGORY =====
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


# ===== TAG =====
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


# ===== ORDER ITEM INLINE (Order ichida chiqadi) =====
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


# ===== PRODUCT =====
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "product_type",
        "category",
        "discount",
    )
    list_filter = ("product_type", "category", "tags")
    search_fields = ("name", "description")
    filter_horizontal = ("tags",)


# ===== ORDER =====
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order_number",
        "customer",
        "qty_products",
        "qty_items",
        "amount",
    )
    search_fields = ("order_number",)
    inlines = [OrderItemInline]


# ===== ORDER ITEM =====
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "order", "total_price")
    search_fields = ("product__name",)