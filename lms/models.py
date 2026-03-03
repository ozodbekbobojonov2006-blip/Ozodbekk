from django.db import models

# Create your models here.
class Teacher (models.Model):
    first_name=models.CharField(verbose_name='ism',max_length=100)
    
    phon_number=models.CharField(verbose_name='telefon nomer',max_length=20)
    staj=models.IntegerField()


    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name='Oqtuvchi'
        verbose_name_plural='Oqtuvchilar'

    
class Student(models.Model):
    full_name=models.CharField(verbose_name='F.I.O',max_length=100)
    age=models.IntegerField(verbose_name='yosh')
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.full_name


class Subject(models.Model):
    name=models.CharField(verbose_name='fan nomi',max_length=100)

    def __str__(self):
        return self.name
    
class SubjectTeacher(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True)
    teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)
        
class Mark(models.Model):
    ball=models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.ball
    
    class Meta:
        verbose_name='baho'
        verbose_name_plural='baholar'