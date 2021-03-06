# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 04:36
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
                ('name', models.CharField(blank=True, editable=False, max_length=50, verbose_name='Акт№')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('invent_number', models.CharField(max_length=50, verbose_name='Инвентарный номер')),
                ('name_host', models.CharField(max_length=50, verbose_name='Имя хоста')),
                ('ipaddr', models.CharField(max_length=50, verbose_name='Ip адресс')),
                ('ffrom', models.CharField(max_length=50, verbose_name='От кого')),
                ('to', models.CharField(max_length=50, verbose_name='Кому')),
                ('description', models.TextField(verbose_name='Примечание')),
                ('number_akt', models.IntegerField(verbose_name='Акт№')),
                ('infotable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KvitokApp.InfoTable', verbose_name='Информациялнные таблицы')),
            ],
            options={
                'verbose_name': 'Квиток',
                'verbose_name_plural': 'Квитки',
                'ordering': ['-number_akt'],
            },
        ),
    ]
