from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Thanks(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    img = models.CharField(max_length=500)

class VThanks(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    img = models.CharField(max_length=500)

