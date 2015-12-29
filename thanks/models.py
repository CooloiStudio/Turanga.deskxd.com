from django.db import models
from home.models import Languages

class Group(models.Model):
    code = models.CharField(max_length=200)
    sort = models.IntegerField(unique=True)

class GroupInfo(models.Model):
    language = models.ForeignKey(Languages)
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=200)


class Thanks(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    img = models.CharField(max_length=500)

class VThanks(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    img = models.CharField(max_length=500)

