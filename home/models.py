from django.db import models

class Special(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)

class SectionHeader(models.Model):
    gamename = models.CharField(max_length=100)
    titleone = models.CharField(max_length=100)
    titletwo = models.CharField(max_length=100)
    img = models.CharField(max_length=500)

class SectionOne(models.Model):
    gamename = models.CharField(max_length=100)
    gametitle = models.CharField(max_length=100)
    textone = models.CharField(max_length=200)
    texttwo = models.CharField(max_length=200)
    img = models.CharField(max_length=500)

class SectionTwo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True)
    img = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

class SectionThree(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True)
    img = models.CharField(max_length=500)
    url = models.CharField(max_length=500)