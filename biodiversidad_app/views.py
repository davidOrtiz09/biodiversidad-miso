# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Species
from .models import UserForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


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


def add_user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')

            user_model = User.objects.create_user(username=username, password=password)
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email
            user_model.save()
            return HttpResponseRedirect(reverse('biodiversidad:index'))
    else:
        form = UserForm()
    context = {
        'form':form
    }
    return render(request, 'biodiversidad_app/_forms/user_registration.html', context)