from django.urls import path
from .views import AddressList

urlpatterns=[
    path('addresses/', AddressList.as_view(), name='address-list'),
]