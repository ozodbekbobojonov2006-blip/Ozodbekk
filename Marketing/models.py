from django.db import models

# Create your models here.
class Market(models.Model):
    name=models.CharField(verbose_name='mahsulot',max_length=100)
    discription=models.CharField(verbose_name='tavsif',max_length=100)
    def __str__(self):
        return self.name

class Customer(models.Model): 
    name1=models.ForeignKey(Market,verbose_name='mahsulot',on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(verbose_name='ism',max_length=100)
    money=models.IntegerField()
    

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='mijoz'
        verbose_name_plural='mijozlar'

      