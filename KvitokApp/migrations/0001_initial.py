# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Информационные Таблицы')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Таблица',
                'verbose_name_plural': 'Таблицы',
            },
        ),
        migrations.CreateModel(
            name='ZapisTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Квитки')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('infotable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KvitokApp.InfoTable', verbose_name='Информациялнные таблицы')),
            ],
            options={
                'verbose_name': 'Квиток',
                'verbose_name_plural': 'Квитки',
                'ordering': ['name'],
            },
        ),
    ]