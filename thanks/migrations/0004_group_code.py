# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thanks', '0003_vthanks'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='code',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
