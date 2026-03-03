from django.db import models

# Create your models here.
class Food(models.Model):
    name=models.CharField(verbose_name='ovqat nomi',max_length=100)
  
    def __str__(self):
        return self.name
    
class breakfast(models.Model):
    name=models.CharField(max_length=100)
    discription=models.CharField(verbose_name='tavsif',max_length=100)

    def __str__(self):
       return self.name

    class Meta:
        verbose_name='nonushta'
        verbose_name_plural='nonushtalar'

class lunch(models.Model):
    name=models.CharField(max_length=100)
    discription=models.CharField(verbose_name='tavsif',max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='tushlik'
        verbose_name_plural='tushliklar'

class dinner(models.Model):
    name=models.CharField(verbose_name='nomi',max_length=100)
    discription=models.CharField(verbose_name='tavsif',max_length=100)

    def __str__(self):
        return self.name
   
    class Meta:
        verbose_name='kechki ovat'
        verbose_name_plural='kechki ovqatlar'

class Menu(models.Model):
    food_id=models.ForeignKey(Food,verbose_name='food',on_delete=models.CASCADE,null=True,blank=True,max_length=100)
    dinner_id=models.ForeignKey(dinner,verbose_name='kechki ovqat',on_delete=models.CASCADE,null=True,blank=True,max_length=100)
    lunch_id=models.ForeignKey(lunch,verbose_name='tushlik',on_delete=models.CASCADE,null=True,blank=True,max_length=100)
    breakfast_id=models.ForeignKey(breakfast,verbose_name='nonushta',on_delete=models.CASCADE,null=True,blank=True,max_length=100)