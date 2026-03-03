from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(verbose_name='restaran nomi',max_length=100)
    email=models.CharField(verbose_name='manzil',max_length=100)
    phone_number=models.CharField(verbose_name='telefon nomer',max_length=100)
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name='Restaran'
        verbose_name_plural='Restaranlar'
class Food(models.Model):
    name=models.CharField(verbose_name='ovqat nomi',max_length=100)   
    money=models.CharField(verbose_name='narxi',max_length=10)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='ovqat'
        verbose_name_plural='ovqatlar'
    
    
class  Customer(models.Model):
    first_name=models.CharField(verbose_name='ism',max_length=100)
    last_name=models.CharField(verbose_name='familya',max_length=100)
    age=models.IntegerField(verbose_name='yosh')
    food=models.ForeignKey(Food,verbose_name='ovqat',on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name='mijoz'
        verbose_name_plural='mijozlar'
    

class Order(models.Model):
    full_name=models.CharField(verbose_name='ism',max_length=100)
    phone_number=models.CharField(verbose_name='tel nomer',max_length=100)
    food=models.ForeignKey(Food,verbose_name='ovqat nomi',on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name='zakaz'
        verbose_name_plural='zakazlar'

