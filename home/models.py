from django.db import models


class Languages(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Menu(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    url = models.CharField(max_length=200)


class MenuInfo(models.Model):
    language = models.ForeignKey(Languages)
    menu = models.ForeignKey(Menu)
    name = models.CharField(max_length=200)


class BasePage(models.Model):
    name = models.CharField(max_length=200, unique=True)
    remark = models.TextField(null=True)

    def __unicode__(self):
        return self.name + "[" + self.remark + "]"


class Section(models.Model):
    code = models.CharField(max_length=100)
    sort = models.IntegerField(unique=True)
    img = models.CharField(max_length=500)
    url = models.CharField(max_length=100)
    basepage = models.ForeignKey(BasePage)


class SectionInfo(models.Model):
    language = models.ForeignKey(Languages)
    section = models.ForeignKey(Section)
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)

