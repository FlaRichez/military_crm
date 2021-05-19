from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=50)
    data_created = models.DateField(auto_now_add=True)
    data_expired = models.DateField()
    status = models.CharField(choices=(
        ('active','active'),
        ('dead','dead'),
    ),max_length=50,default='active')
    document_root = models.CharField(choices=(
        ('public','public'),
        ('private','private'),
        ('secret','secret'),
        ('top-secret','top-secret'),
    ),max_length=50)
