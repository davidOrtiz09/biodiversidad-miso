# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biodiversidad_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('comment', models.TextField(max_length=1000, verbose_name='Comentario')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creaci\xf3n')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
        migrations.AlterModelOptions(
            name='species',
            options={'verbose_name': 'Especie', 'verbose_name_plural': 'Especies'},
        ),
        migrations.RenameField(
            model_name='species',
            old_name='category_id',
            new_name='fk_category',
        ),
        migrations.AlterField(
            model_name='species',
            name='long_description',
            field=models.TextField(max_length=300, verbose_name='Descripci\xf3n larga'),
        ),
        migrations.AlterField(
            model_name='species',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='species',
            name='picture',
            field=models.ImageField(upload_to='species-images', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='species',
            name='scientific_name',
            field=models.CharField(max_length=150, verbose_name='Nombre cient\xedfico'),
        ),
        migrations.AlterField(
            model_name='species',
            name='short_description',
            field=models.TextField(max_length=150, verbose_name='Descripci\xf3n corta'),
        ),
        migrations.AlterField(
            model_name='species',
            name='taxonomic_classification',
            field=models.CharField(max_length=150, verbose_name='Clasificaci\xf3n taxon\xf3mica'),
        ),
        migrations.AddField(
            model_name='comment',
            name='fk_species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biodiversidad_app.Species', verbose_name='Especie'),
        ),
    ]
