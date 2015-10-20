# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thanks', '0002_remove_thanks_img_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='VThanks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=500)),
                ('img', models.CharField(max_length=500)),
            ],
        ),
    ]
