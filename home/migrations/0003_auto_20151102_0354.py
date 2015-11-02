# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20151102_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionone',
            name='textone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sectionone',
            name='texttwo',
            field=models.CharField(max_length=200),
        ),
    ]
