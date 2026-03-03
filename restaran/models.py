from django.db import models

# Create your models here.
class dinner(models.Model):
    name=models.CharField(verbose_name='nomi',max_length=100)
    discription=models.CharField(verbose_name='tavsif',max_length=100)
    locetion=models.CharField(verbose_name='joylashuv',max_length=25)
    price=models.IntegerField(verbose_name='narxi')
    bonus=models.CharField(verbose_name='sovga',max_length=25)

    def __str__(self):
        return self.name
   
    class Meta:
        verbose_name='kechki ovat'
        verbose_name_plural='kechki ovqatlar'


class lunch(models.Model):
    name=models.CharField(verbose_name='ovqat nomi',max_length=100)
    discription=models.TextField(verbose_name='tavsif')
    phone_number=models.CharField(verbose_name='telefon nomer',max_length=20)
    email=models.EmailField()
    locetion=models.CharField(verbose_name='manzil',max_length=25)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name='tushlik'
        verbose_name_plural='tushliklar'

class breakfast(models.Model):
    name=models.CharField(verbose_name='ovqat nomi',max_length=100)
    discription=models.TextField(verbose_name='tavsif')
    activity=models.BooleanField(verbose_name='faolligi',default=True)
    phone_number=models.CharField(verbose_name='telefon nomer',max_length=20)
    email=models.EmailField()
    def __str__(self):
       return self.name

    class Meta:
        verbose_name='nonushta'
        verbose_name_plural='nonushtalar'


class Product(models.Model):
    breakfast=models.ForeignKey(breakfast,verbose_name='nonushta',on_delete=models.CASCADE,null=True,blank=True)
    lunch=models.ForeignKey(lunch,verbose_name='tushlik',on_delete=models.CASCADE,null=True,blank=True)
    dinner=models.ForeignKey(dinner,verbose_name='kechki ovqat',on_delete=models.CASCADE,null=True,blank=True)
    oshpaz=models.CharField('kim qilganligi',max_length=100)
    phone_number=models.CharField(verbose_name='telefon nomer',max_length=20)
    locetion=models.CharField(verbose_name='joylashuv',max_length=25)
    
    def __str__(self):
        return self.oshpaz
    class Meta:
        verbose_name='maxsulot'
        verbose_name_plural='maxsulotlar'

class Delivery_driver(models.Model):
    first_name=models.CharField(verbose_name='ism',max_length=20)
    last_name=models.CharField(verbose_name='familya',max_length=20)
    car=models.CharField(verbose_name='moshina turi',max_length=20)
    phone_number=models.CharField(verbose_name='telefon nomer',max_length=20)
    passport=models.CharField(verbose_name='pasport raqam',max_length=20)
    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name='dastafchik'
        verbose_name_plural='dastafchiklar'


class online(models.Model):
    name=models.CharField(verbose_name='ism',max_length=30)
    breakfast=models.ForeignKey(breakfast,verbose_name='nonushta',on_delete=models.CASCADE,null=True,blank=True)
    lunch=models.ForeignKey(lunch,verbose_name='tushlik',on_delete=models.CASCADE,null=True,blank=True)
    dinner=models.ForeignKey(dinner,verbose_name='kechki ovqat',on_delete=models.CASCADE,null=True,blank=True)
    price=models.IntegerField()
    phone_number=models.CharField(verbose_name='telefon nomer',max_length=25)
    zakaz=models.BooleanField(verbose_name='yetb borganligi haqida')
    delivery=models.ForeignKey(Delivery_driver,verbose_name='yetqazib beruvchi',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='dastafka'
        verbose_name_plural='dastafkalar'
