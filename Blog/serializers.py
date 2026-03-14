from .models import Address,Post
from rest_framework import serializers

class AdressSerilazers(serializers.ModelSerializer):
    name=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Address
        fields=['city','country','name']

    def get_name(self,obj):
        return f'{obj.city} {obj.street}'    

class postserializers(serializers.ModelSerializer):
    name=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Post
        fields='__all__'
              
