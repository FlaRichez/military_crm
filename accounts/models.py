from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Dossier(models.Model):
    fullname = models.CharField(max_length=50)
    date_birth = models.DateField()
    image = models.ImageField()
    gender = models.CharField(choices=(
        ('M','M'),
        ('F','F'),
    ),max_length=50)
    user = models.OneToOneField(User,on_delete=models.PROTECT)


class Car(models.Model):
    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.DateField()
    number = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    dossier = models.ForeignKey(Dossier,on_delete=models.CASCADE,related_name='cars')


class Education(models.Model):
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    school_name = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
    dossier = models.ForeignKey(Dossier,on_delete=models.CASCADE,related_name='education')


class Warcraft(models.Model):
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    military_area = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    start_pose = models.DateField(auto_now=True)
    end_pose = models.DateField()
    dossier = models.ForeignKey(Dossier,on_delete=models.CASCADE,related_name='warcraft')


