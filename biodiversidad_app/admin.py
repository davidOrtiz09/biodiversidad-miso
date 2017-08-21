# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from biodiversidad_app.models import Species, Comment, AppUser, Category


class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('date_created', )


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scientific_name')
    list_display_links = ('id', 'name', 'scientific_name')
    search_fields = ('name', 'scientific_name')
    # list_filter = ('fk_category', )
    inlines = (CommentsInline, )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date_created')
    list_display_links = ('id', 'email')
    search_fields = ('email', )
    list_filter = ('date_created', )
    readonly_fields = ('date_created', )


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'city', 'country')
    list_display_links = ('id', 'username')
    list_filter = ('city', 'country')
    filter_horizontal = ('favorites_species', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.site_title = 'Biodiversidad G2'
admin.site.site_header = 'Biodiversidad G2'
admin.site.index_title = 'Procesos ágiles de desarrollo: Grupo 2'

admin.site.register(Species, SpeciesAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(AppUser, UserAdmin)
admin.site.register(Category, CategoryAdmin)
