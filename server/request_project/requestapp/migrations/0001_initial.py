# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('address', models.CharField(max_length=255)),
                ('address_number', models.CharField(max_length=30)),
                ('reference', models.TextField(null=True)),
                ('document', models.CharField(max_length=14, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('imei', models.CharField(max_length=18, serialize=False, primary_key=True)),
                ('last_request_id', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('city', models.ForeignKey(to='requestapp.City')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('abbreviation', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='requestapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('address_number', models.CharField(max_length=30)),
                ('reference', models.TextField(null=True)),
                ('device_request_id', models.IntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('observation', models.TextField(null=True)),
                ('client', models.ForeignKey(to='requestapp.Client')),
                ('device', models.ForeignKey(to='requestapp.Device', null=True)),
                ('district', models.ForeignKey(to='requestapp.District')),
            ],
        ),
        migrations.CreateModel(
            name='RequestItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.PositiveIntegerField(default={'max_value': 10, 'min_value': 1})),
                ('item', models.ForeignKey(to='requestapp.Item')),
                ('request', models.ForeignKey(to='requestapp.Request')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='district',
            field=models.ForeignKey(to='requestapp.District'),
        ),
        migrations.AddField(
            model_name='city',
            name='estado',
            field=models.ForeignKey(to='requestapp.Estado'),
        ),
    ]
