from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    passport_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    
class Avtomobil(models.Model):
    model = models.CharField(max_length=100)
    raqam = models.CharField(max_length=20)

    def __str__ (self):
        return 'malumot'
    
class Malumot(models.Model):
    ism=models.CharField(max_length=100)
    familya=models.CharField(max_length=100)


    def __str__(self):
        return self.ism

    class Meta:
        verbose_name='Malumot'
        verbose_name_plural='Malumotlar'
        
class Moshina(models.Model):
    modeli = models.ForeignKey(Malumot, on_delete=models.CASCADE)
    def __str__(self):
        return 'toliq malumot'
    class Meta:
        verbose_name= 'Moshina'
        verbose_name_plural='Moshinalar'
