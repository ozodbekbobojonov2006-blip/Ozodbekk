from django.urls import path
from .views import ProductListApiView, ProductPostApiView

urlpatterns = [
   path('products/', ProductListApiView.as_view(), name='product-list'),
   path('product-post/', ProductPostApiView.as_view(), name='product-post'),
]