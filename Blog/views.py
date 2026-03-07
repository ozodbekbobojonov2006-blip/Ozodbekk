from django.shortcuts import render

from .serializers import  AdressSerilazers
from .models import Address
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class AddressList(APIView):
    def get(self, request):
        addresses=Address.objects.all()
        serializer=AdressSerilazers(addresses, many=True)
        return Response(serializer.data)
    