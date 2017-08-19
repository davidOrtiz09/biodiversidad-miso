# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from biodiversidad_app.models import Species


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scientific_name')
    list_display_links = ('id', 'name', 'scientific_name')
    search_fields = ('name', 'scientific_name')

admin.site.site_title = 'Procesos ágiles de desarrollo: Grupo 4'
admin.site.site_header = 'Header'
admin.site.index_title = 'Index'

admin.site.register(Species, SpeciesAdmin)
