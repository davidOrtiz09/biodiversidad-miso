# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.transaction import atomic
from django.template.loader import get_template
from biodiversidad_app.models import Species, Category, Comment, AppUser
from biodiversidad_app.forms import UserForm, UserFormUpdate
from biodiversidad_app.utils import send_html_mail


def index(request):
    category_list = Category.objects.all()
    form = UserForm()
    context = {'category_list': category_list, 'form': form}
    return render(request, 'biodiversidad_app/index.html', context)


class Login(View):
    def post(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('biodiversidad:index'))

        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
        else:
            messages.add_message(request, messages.WARNING, 'Por favor verifique el nombre de usuario y la contraseña')
        return redirect(reverse('biodiversidad:index'))


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('biodiversidad:index'))


def specie_view(request, species_id=None):
    species = Species.objects.filter(id=species_id).first()
    if species:
        comments = Comment.objects.filter(fk_species=species.id)
        context = {
            'specie': species,
            'comments': comments,
            'form': UserForm()
        }
        return render(request, 'biodiversidad_app/verEspecie.html', context)
    else:
        messages.add_message(request, messages.WARNING, 'Lo sentimos, no encontramos la especie que estabas buscando')
        return redirect(reverse('biodiversidad:index'))


@atomic
def add_user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            email = cleaned_data.get('email')
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            password = cleaned_data.get('password')
            city = cleaned_data.get('city')
            country = cleaned_data.get('country')
            picture = cleaned_data.get('picture')
            interest = cleaned_data.get('interest')

            user_model = User.objects.create_user(
                username=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            user_model.save()

            app_user_model = AppUser(fk_django_user=user_model, picture=picture, city=city, country=country, interest=interest)
            app_user_model.save()
            template = get_template('biodiversidad_app/emails/welcome.html')
            content = template.render({
                'name': '{0} {1}'.format(first_name, last_name)
            })
            send_html_mail('Bienvenido a Biodiversidad G2', content, [email])

            return HttpResponseRedirect(reverse('biodiversidad:index'))
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'biodiversidad_app/_forms/user_registration.html', context)


@atomic
def update_user_view(request):
    if request.method == 'POST':
        form = UserFormUpdate(request.POST, request.FILES)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            email = cleaned_data.get('email')
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            password = cleaned_data.get('password')
            city = cleaned_data.get('city')
            country = cleaned_data.get('country')
            interest = cleaned_data.get('interest')

            user_model = User.objects.get(username=request.user.username, password=request.user.password)
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email

            if password != '':
                user_model.set_password(password)

            user_model.save()

            app_user_model = AppUser.objects.get(fk_django_user=user_model)
            app_user_model.city = city
            app_user_model.country = country
            app_user_model.interest = interest

            app_user_model.save()
            return redirect(reverse('biodiversidad:index'))
    else:
        form = UserFormUpdate()
        user_model = User.objects.get(username=request.user.username, password=request.user.password)
        app_user_model = AppUser.objects.get(fk_django_user=user_model)
        form.fields["first_name"].initial = request.user.first_name
        form.fields["last_name"].initial = request.user.last_name
        form.fields["email"].initial = request.user.email
        form.fields["city"].initial = app_user_model.city
        form.fields["country"].initial = app_user_model.country
        form.fields["interest"].initial = app_user_model.interest
    context = {
        'form': form
    }
    return render(request, 'biodiversidad_app/_forms/user.html', context)


@atomic
def add_comment(request, species_id):
    try:
        if request.method == 'POST':
            email = request.POST.get('email', '')
            comentario = request.POST.get('comentario', '')
            specie_model = Species.objects.get(id=species_id)
            comment_model = Comment(fk_species=specie_model, email=email, comment=comentario)
            comment_model.save()
            return redirect(reverse('biodiversidad:index'))
    except:
        return redirect(reverse('biodiversidad:index'))
