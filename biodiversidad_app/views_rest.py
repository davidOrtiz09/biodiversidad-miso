# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from biodiversidad_app.models import Species


def index(request):
    return JsonResponse({'status': 'ok'})


def get_species_by_category(request):
    id_categoria = request.GET.get('id_categoria', '')
    species = Species.objects.all()
    if id_categoria != '':
        species = species.filter(fk_category_id=id_categoria)

    species_list = [x.to_json() for x in species]
    return JsonResponse({'species': species_list})
