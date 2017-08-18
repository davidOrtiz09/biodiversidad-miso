# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Species(models.Model):
    category_id = models.CharField(max_length=150, blank=False)  # TODO: Crear la fx cuando las categorias sean creadas
    name = models.CharField(max_length=150, blank=False)
    picture = models.ImageField(upload_to='images', null=False)
    short_description = models.CharField(max_length=150, blank=False)
    long_description = models.CharField(max_length=300, blank=False)
    scientific_name = models.CharField(max_length=150, blank=False)
    taxonomic_classification = models.CharField(max_length=150, blank=False)




