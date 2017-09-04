# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.forms import forms
from django.forms import ModelForm
from biodiversidad_app.models import AppUser

class AbstractUserForm(ModelForm):
    first_name = forms.CharField(max_length=User._meta.get_field('first_name').max_length, label='Nombres')
    last_name = forms.CharField(max_length=User._meta.get_field('last_name').max_length, label='Apellidos')
    email = forms.EmailField(label='Correo electrónico')
    city = forms.CharField(max_length=100, label='Ciudad')
    country = forms.CharField(max_length=100, label='País')
    picture = forms.ImageField(label='Imagen de perfil')
    interest = forms.CharField(widget=forms.Textarea(), max_length=1000, label='Interés')
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirma tu contraseña')

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las claves no coinciden.')
        return password2


class UserForm(AbstractUserForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'city', 'country', 'interest', 'password', 'password2', 'picture']

    def clean_username(self):

        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado. ')
        return username

    def clean_email(self):

        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual registrado. ')
        return email


class UserFormUpdate(AbstractUserForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'city', 'country', 'interest', 'password', 'password2']
