# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermercado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='idProduto',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='supermercado',
            name='idSupermercado',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idUsuario',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
