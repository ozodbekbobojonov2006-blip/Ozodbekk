from django.shortcuts import render
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .serializers import AdressSerilazers,postserializers
from .models import Address,Post
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView


# Create your views here.

class AddressList(APIView):
    def get(self, request):
        addresses = Address.objects.all() # queryset[]
        serializer = AdressSerilazers(addresses, many=True)
        return Response(serializer.data)


class AddressPost(APIView):
    def post(self, request):
        serializer =AdressSerilazers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdressCreate(ListCreateAPIView):
    queryset = Address.objects.filter(city='Tashkent')
    serializer_class = AdressSerilazers


class PostList(APIView):
    def get(self, request):
        posts=Post.objects.all()
        serializer=postserializers(posts, many=True)
        return Response(serializer.data)
    
class Postlar(APIView):
    def post(self,request):
        serializer=postserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)