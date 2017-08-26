from django.contrib.auth.forms import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class UserForm(ModelForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']

    def clean_username(self):

        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado. ')
        return username

    def clean_email(self):

        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya exsiste un email igual registrado. ')
        return email

    def clean_password2(self):

        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las claves no coinciden.')
        return password2

