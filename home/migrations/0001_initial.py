# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SectionHeader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gamename', models.CharField(max_length=100)),
                ('titleone', models.CharField(max_length=100)),
                ('titletwo', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SectionOne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gamename', models.CharField(max_length=100)),
                ('gametitle', models.CharField(max_length=100)),
                ('textone', models.CharField(max_length=100)),
                ('texttwo', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SectionThree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SectionTwo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=500)),
            ],
        ),
    ]
