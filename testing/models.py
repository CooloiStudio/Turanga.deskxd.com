from django.db import models
from home.models import Languages

class UserMessage(models.Model):
    email = models.CharField(max_length=500)
    issend = models.BooleanField(default=False)
    datatime = models.DateTimeField()


class Platform(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    img = models.CharField(max_length=500)
    url = models.CharField(max_length=100)
    version = models.CharField(max_length=200)

    def __unicode__(self):
        return self.code


class Versions(models.Model):
    platform = models.ForeignKey(Platform)
    sort = models.IntegerField(unique=True)
    versions = models.CharField(max_length=100)


class VersionInfo(models.Model):
    vs = models.ForeignKey(Versions)
    language = models.ForeignKey(Languages)
    info = models.TextField(null=True)