

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
class akount(models.Model):
    name=models.CharField(verbose_name='ism',max_length=25)
    last_name=models.CharField(verbose_name='familya',max_length=25)
    age=models.IntegerField(default=0)
    email=models.EmailField(null=True,blank=True)
    detail=models.TextField(null=True,blank=True)
    malumot=models.CharField(verbose_name='umumiy malumot',max_length=100,null=True,blank=True)


    @property
    def user(self):
        return f'{self.name}, {self.last_name}, {self.age},{self.detail}'
    
    def save(self,*args, **kwargs):
        self.malumot=self.user
        return super(akount,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user=models.ForeignKey(akount,on_delete=models.CASCADE,null=True,blank=True,verbose_name='akkount')
    phone_number=models.CharField(verbose_name='telefon raqam',max_length=25)
    lacation=models.CharField(verbose_name='lakatsiya',max_length=100)
    image=models.ImageField(verbose_name='rasm uchun joy',upload_to='profiles/', max_length=255)
    birth_day=models.DateTimeField(auto_now=True)
    
class employee(models.Model):
    profile=models.ForeignKey(akount,verbose_name='kmni ishchilari',on_delete=models.CASCADE)
    name=models.CharField(verbose_name='ism',max_length=30)
    last_name=models.CharField(verbose_name='familya',max_length=190)
    age=models.IntegerField(verbose_name='yosh')
    position=models.CharField(verbose_name='lavozim',max_length=99)
    haqida=models.TextField(verbose_name='malumot',max_length=199)
    image=models.ImageField(verbose_name='rasm uchun joy')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name='hodim'
        verbose_name_plural='hodimlar'
        



class Position(models.Model):
    ega=models.ForeignKey(akount,on_delete=models.CASCADE,verbose_name='boshliq')
    Position_name=models.CharField(verbose_name='lavozim turi',max_length=100)
    www=RichTextField(verbose_name='ish haqida')
    is_active = models.BooleanField(default=True, verbose_name='hozir bormi bunday lavozim')
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.Position_name


    class Meta:
        verbose_name='lavozim'
        verbose_name_plural='lavozimlar'

class Monthly(models.Model):
    name=models.ForeignKey(akount,on_delete=models.CASCADE,related_name='monthly_entries',verbose_name='ishchi')
    employe=models.OneToOneField(employee,verbose_name='hodim',on_delete=models.CASCADE)
    position=models.ForeignKey(Position,on_delete=models.CASCADE,null=True,blank=True,verbose_name='lavozim')
    money=models.IntegerField(verbose_name='ish haqi')
    bonus=models.CharField(max_length=100)
    id_active=models.BooleanField(default=True,verbose_name='berilgan berilmaganligi')
    
    def __str__(self):
        return self.bonus
    
    class Meta:
        verbose_name='oylik'
        verbose_name_plural='oyliklar'

class Attendance(models.Model):
    email=models.CharField(max_length=100)
    worker = models.ForeignKey(akount, on_delete=models.CASCADE, verbose_name='ishchi',null=True,blank=True)
    money=models.ForeignKey(Monthly,on_delete=models.CASCADE,null=True,blank=True,verbose_name='ish haqi')
    date = models.DateTimeField(default=timezone.now)
    is_active=models.BooleanField(default=True,verbose_name='kelgan kelmaganligi haqida')
    comment = models.TextField(blank=True, verbose_name='izoh',null=True)
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name='davomat'
        verbose_name_plural='davomatlar'



class grade (models.Model):
    profile=models.ForeignKey(employee,verbose_name='hodimlar roxati',on_delete=models.CASCADE)
    ega=models.IntegerField(verbose_name='baho')
    comment=models.TextField(max_length=100)
    is_active=models.BooleanField(default=True,verbose_name='tasdiqlash')

class tasks (models.Model):
    profile=models.ForeignKey(employee,on_delete=models.CASCADE,verbose_name='ism')
    task=models.TextField(max_length=100,verbose_name='vazifa')
    
    class Meta:
        verbose_name='vazifa'
        verbose_name_plural='vazifalar'


class projects(models.Model):
    profile=models.OneToOneField(employee,on_delete=models.CASCADE,verbose_name='ism')
    project=models.TextField(max_length=100)
    task=models.OneToOneField(tasks,on_delete=models.CASCADE,verbose_name='vazifani bajarish shartlari')

    class Meta:
        verbose_name='proyekt'
        verbose_name_plural='proyektlar' 

class Warnings(models.Model):
    name=models.ManyToManyField(employee,verbose_name='ism')
    reason=models.TextField(max_length=100,verbose_name='sababi')
    money=models.IntegerField(verbose_name='summa')
    is_active=models.BooleanField(default=True,verbose_name='tasdiq')
    
# class product(models.Model):
#     name=models.CharField(verbose_name='ism',max_length=100)
#     price=models.IntegerField(verbose_name='narx')
#     surog=models.CharField(max_length=100)
#
# class category(models.Model):
#     name=models.ForeignKey(product,on_delete=models.CASCADE,verbose_name='narx')
#     description=models.TextField(max_length=100,verbose_name='narx')
#
#
# class order(models.Model):
#     order_number=models.IntegerField(verbose_name='narx')
#     product=models.ForeignKey(product,on_delete=models.CASCADE,verbose_name='maxsulot')
#     time=models.DateTimeField(auto_now=True)
#     narx_turi=models.CharField(max_length=100,verbose_name='narx')
#     qarz=models.TextField(max_length=100,verbose_name='qarz')
#     is_active=models.BooleanField(default=True,verbose_name='tasdiq')
#
#
# class order_items(models.Model):
#     product=models.ForeignKey(product,on_delete=models.CASCADE,verbose_name='maxsulot')
#     time=models.DateTimeField(auto_now=True)
#     order=models.ForeignKey(order,on_delete=models.CASCADE,verbose_name='narx')
#















