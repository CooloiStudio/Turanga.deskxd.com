from django.db import models
from DjangoUeditor.models import UEditorField

class Agreement(models.Model):
    content = UEditorField(u'test',width=1200, height=600, toolbars="full", imagePath="", filePath="", upload_settings={"imageMaxSize":1204000}, settings={}, command=None, event_handler=myEventHander(), blank=True)
