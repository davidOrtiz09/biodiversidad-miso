# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View
from django.shortcuts import render
from .models import Species


class Index(View):
    def get(self, request):
        species_list = Species.objects.all()
        context = {'species_list': species_list}
        return render(request, 'biodiversidad_app/index.html', context)
