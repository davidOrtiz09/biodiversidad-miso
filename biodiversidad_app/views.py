# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Species


class Index(View):
    def get(self, request):
        species_list = Species.objects.all()
        context = {'species_list': species_list}
        return render(request, 'biodiversidad_app/index.html', context)


def login_view(request):

    if request.user.is_authenticated():
        return redirect(reverse('biodiversidad:index'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('biodiversidad:index'))
        else:
            mensaje = 'Nombre de usuario o clave invalido'

    return render(request, 'biodiversidad_app/_elements/_log-in.html', {'mensaje': mensaje})

def specie_view(request, id = None):
    try:
        specie = Species.objects.get(id = id)
        context = {'specie': specie}
        return render(request, 'biodiversidad_app/verEspecie.html', context)
    except:
        return redirect(reverse('biodiversidad:index'))