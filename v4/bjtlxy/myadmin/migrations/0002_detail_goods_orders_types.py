# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-06 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.IntegerField()),
                ('goodsid', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('num', models.IntegerField()),
            ],
            options={
                'db_table': 'detail',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.IntegerField()),
                ('goods', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=50)),
                ('descr', models.TextField()),
                ('price', models.FloatField()),
                ('picname', models.CharField(max_length=255)),
                ('state', models.IntegerField(default=1)),
                ('store', models.IntegerField(default=0)),
                ('num', models.IntegerField(default=0)),
                ('clicknum', models.IntegerField(default=0)),
                ('addtime', models.IntegerField()),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('linkman', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=16)),
                ('addtime', models.IntegerField()),
                ('total', models.FloatField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('pid', models.IntegerField(default=0)),
                ('path', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'type',
            },
        ),
    ]
