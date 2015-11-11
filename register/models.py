from django.db import models
from DjangoUeditor.models import UEditorField

class Agreement(models.Model):
    content = UEditorField(u'test',width=1200, height=600, toolbars="full", settings={}, command=None, blank=True)
