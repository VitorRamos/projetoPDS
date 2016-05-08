# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Possui',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('preco', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('idProduto', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('marca', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Supermercado',
            fields=[
                ('idSupermercado', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('localizacao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('senha', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='supermercado.Usuario')),
                ('CPF', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Empresario',
            fields=[
                ('idEmpresario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='supermercado.Usuario')),
                ('CPF', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='possui',
            name='idProduto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermercado.Produto'),
        ),
        migrations.AddField(
            model_name='possui',
            name='idSupermercado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermercado.Supermercado'),
        ),
        migrations.AddField(
            model_name='favorito',
            name='idProduto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermercado.Produto'),
        ),
        migrations.AddField(
            model_name='dono',
            name='idSupermercado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermercado.Supermercado'),
        ),
        migrations.AlterUniqueTogether(
            name='possui',
            unique_together=set([('idSupermercado', 'idProduto')]),
        ),
        migrations.AddField(
            model_name='favorito',
            name='idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermercado.Cliente'),
        ),
        migrations.AddField(
            model_name='dono',
            name='idEmpresaio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermercado.Empresario'),
        ),
        migrations.AlterUniqueTogether(
            name='favorito',
            unique_together=set([('idCliente', 'idProduto')]),
        ),
        migrations.AlterUniqueTogether(
            name='dono',
            unique_together=set([('idEmpresaio', 'idSupermercado')]),
        ),
    ]
