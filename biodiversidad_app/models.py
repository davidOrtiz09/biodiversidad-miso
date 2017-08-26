# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Categoría', null=False, blank=False)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Species(models.Model):
    fk_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría', null=False, blank=False)
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True, null=False, blank=False)
    scientific_name = models.CharField(max_length=150, verbose_name='Nombre científico', unique=True, null=False, blank=False)
    taxonomic_classification = models.CharField(max_length=150, verbose_name='Clasificación taxonómica', null=False, blank=False)
    picture = models.ImageField(upload_to='species-images', verbose_name='Imagen', null=False, blank=False)
    short_description = models.TextField(max_length=150, verbose_name='Descripción corta', null=False, blank=False)
    long_description = models.TextField(max_length=300, verbose_name='Descripción larga', null=False, blank=False)

    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
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


@python_2_unicode_compatible
class AppUser(models.Model):
    fk_django_user = models.OneToOneField(User, verbose_name='Usuario del sistema', null=False, blank=False)
    picture = models.ImageField(upload_to='user-pictures', verbose_name='Foto', null=False, blank=False)
    city = models.CharField(max_length=100, verbose_name='Ciudad', null=False, blank=False)
    country = models.CharField(max_length=100, verbose_name='Pais', null=False, blank=False)
    interest = models.TextField(max_length=1000, verbose_name='Interés', null=True, blank=True)

    favorites_species = models.ManyToManyField(Species, verbose_name='Especies favoritas', blank=True)

    class Meta:
        verbose_name = 'Usuario de la aplicación'
        verbose_name_plural = 'Usuarios de la aplicación'

    @property
    def first_name(self):
        return self.fk_django_user.first_name

    @property
    def last_name(self):
        return self.fk_django_user.last_name

    @property
    def username(self):
        return self.fk_django_user.username

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
