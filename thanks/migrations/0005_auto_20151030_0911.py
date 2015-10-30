# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thanks', '0004_group_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='code',
            field=models.IntegerField(unique=True),
        ),
    ]
