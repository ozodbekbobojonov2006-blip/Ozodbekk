from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer, ProductPostSerilSerializer

from django.db.models import Sum
# Create your views here.

class ProductListApiView(APIView):

    def get(self, request, format=None):
        products =  Product.objects.annotate(total_sold=Sum('orderitem__quantity')).order_by('-total_sold')[:5]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)



class ProductPostApiView(APIView):
    def post(self, request, format=None):
        serializer = ProductPostSerilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

