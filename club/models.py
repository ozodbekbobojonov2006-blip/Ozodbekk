from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=200)
    rasm=models.ImageField(upload_to='sovrinlar',null=True,blank=True)
    def __str__(self):
        return self.name
class ClubMember(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class arsenal(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)