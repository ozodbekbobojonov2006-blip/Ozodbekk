from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(verbose_name='ism',max_length=100)
    experience = models.IntegerField(verbose_name='staj')  # yil
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Oqtuvchi'
        verbose_name_plural='oqtuvchilar'

class Subject(models.Model):
    name = models.CharField(verbose_name='ism',max_length=100)
    teacher = models.ForeignKey(Teacher,verbose_name='oqtuvchisi', on_delete=models.CASCADE)
    class Meta:
        verbose_name='fan'
        verbose_name_plural='fanlar'
    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(verbose_name='ism',max_length=100)
    age = models.IntegerField(verbose_name='yosh')
    subjects = models.ManyToManyField(Subject)
    class Meta:
        verbose_name='talaba'
        verbose_name_plural='talabalar'
    def __str__(self):
        return self.name
class Grade(models.Model):
    student = models.ForeignKey(Student,verbose_name='talaba', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,verbose_name='mavzu', on_delete=models.CASCADE)
    grade = models.IntegerField(verbose_name='ball')
    date = models.DateField(verbose_name='sana',auto_now_add=True)
    def __str__(self):
       return f"{self.student.name} - {self.grade}"
    class Meta:
        verbose_name='Ball'
        verbose_name_plural='Ballar'