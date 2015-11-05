from django.db import models

class UserMessage(models.Model):
    email = models.CharField(max_length=500)
    issend = models.BooleanField(default=False)
