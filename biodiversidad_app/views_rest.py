# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from biodiversidad_app.models import Species, AppUser
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return JsonResponse({'status': 'ok'})


def get_species_by_category(request):
    id_categoria = request.GET.get('id_categoria', '')
    species = Species.objects.all()
    if id_categoria != '':
        species = species.filter(fk_category_id=id_categoria)

    species_list = [x.to_json() for x in species]
    return JsonResponse({'species': species_list})


@csrf_exempt
def add_favorite(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        usuario = AppUser.objects.filter(fk_django_user__email=body["user"]).first()
        especie = Species.objects.filter(id=body["specie"]).first()
        if usuario and especie:
            usuario.favorites_species.add(especie)
            usuario.save()
        return JsonResponse({"mensaje": "OK"})
