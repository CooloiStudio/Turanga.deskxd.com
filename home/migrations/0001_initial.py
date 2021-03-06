# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('remark', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('sort', models.IntegerField(unique=True)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MenuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Languages')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('sort', models.IntegerField(unique=True)),
                ('img', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=100)),
                ('basepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.BasePage')),
            ],
        ),
        migrations.CreateModel(
            name='SectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('subtitle', models.CharField(max_length=200, null=True)),
                ('text', models.TextField(null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Languages')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Section')),
            ],
        ),
    ]
