from django.db import models


class sovrinlar(models.Model):
    name=models.CharField(max_length=200)
    qita=models.CharField(max_length=200)
    rasmi=models.ImageField(upload_to='sovrinlar',null=True,blank=True)
    haqida=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class liga(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class davlat(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class kamanda(models.Model):
    name=models.CharField(max_length=200)
    liga=models.ForeignKey(liga,on_delete=models.CASCADE)
    sovrinlar=models.ForeignKey(sovrinlar,on_delete=models.CASCADE)
    murabbiy=models.CharField(max_length=200)
    ochko=models.IntegerField(default=0)
    city=models.CharField(max_length=200)
    stadion=models.CharField(max_length=200)
    logo=models.ImageField(upload_to='kamanda',null=True,blank=True)
    tashkil_topgan=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class oyincilar(models.Model):
   name=models.CharField(max_length=200)
   nomer=models.IntegerField()
   kamanda=models.ForeignKey(kamanda,on_delete=models.CASCADE)
   davlat=models.ForeignKey(davlat,on_delete=models.CASCADE)
   gollar=models.IntegerField()
   asiste=models.IntegerField()
   boyi=models.IntegerField()
   vazni=models.IntegerField()
   rasmi=models.ImageField(upload_to='oyincilar',null=True,blank=True)

   def __str__(self):
        return self.name


class pazitsiya(models.Model):
    name=models.CharField(max_length=200)
    oyincilar=models.ForeignKey(oyincilar,on_delete=models.CASCADE)

class bozor (models.Model):
    name=models.OneToOneField(oyincilar,on_delete=models.CASCADE)
    narxi=models.IntegerField()
    def __str__(self):
        return str('self.oyincilar')
