from django.urls import path
from .views import AddressList, AddressPost,AdressCreate,PostList,Postlar

urlpatterns = [
    path('addresses/', AddressList.as_view(), name='address-list'),
    path('address/post/', AddressPost.as_view(), name='address-post'),
    path('create/', AdressCreate.as_view(), name='adress-create'),
    path('post', PostList.as_view(), name='post'),
    path('postt', Postlar.as_view(), name='postlar')
]