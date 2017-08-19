# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Species(models.Model):
    fk_category = models.CharField(max_length=150, blank=False)  # TODO: Crear la fx cuando las categorias sean creadas
    # fk_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría', null=True, blank=True) # Campo propuesto (podría cambiar)
    name = models.CharField(max_length=150, verbose_name='Nombre', null=False, blank=False)
    picture = models.ImageField(upload_to='species-images', verbose_name='Imagen', null=False, blank=False)
    short_description = models.TextField(max_length=150, verbose_name='Descripción corta', null=False, blank=False)
    long_description = models.TextField(max_length=300, verbose_name='Descripción larga', null=False, blank=False)
    scientific_name = models.CharField(max_length=150, verbose_name='Nombre científico', null=False, blank=False)
    taxonomic_classification = models.CharField(max_length=150, verbose_name='Clasificación taxonómica', null=False, blank=False)

    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'

    def __str__(self):
        return self.name


class Comment(models.Model):
    fk_species = models.ForeignKey(Species, on_delete=models.CASCADE, verbose_name='Especie', null=False, blank=False)
    email = models.EmailField(max_length=150, verbose_name='Email', null=False, blank=False)
    comment = models.TextField(max_length=1000, verbose_name='Comentario', null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación', editable=False, null=False, blank=False)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return 'Comentario de {0} sobre la especie {1}'.format(self.email, self.fk_species.name)
