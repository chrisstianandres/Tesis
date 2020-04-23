from django import forms
from apps.docente.models import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import *

class DocenteForm(UserCreationForm):
    class Meta:

        model = Docente
        fields = [
            'rol',
            'username',
            'first_name',
            'last_name',
            'email',
            'cedula',
            'telefono',
            'direccion',
            'avatar',
            'password1',
            'password2',

        ]
        labels = {
            'rol': 'Rol',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Correo',
            'cedula': 'N° de Cédula',
            'telefono': 'N° de Teléfono',
            'direccion': 'Direccion',

        }
        widgets = {
            'rol': forms.Select(attrs={'class': 'selectpicker', 'data-width': '100%'}),
            'username': forms.TextInput(attrs={'class': 'form-control form-rounded'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-rounded'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-rounded'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-rounded'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control form-rounded'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-rounded'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control form-rounded'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-rounded',  'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-rounded'}),
        }


