from django import forms
from datetime import *
#from django.forms import extras
from django.forms import SelectDateWidget, TextInput, NumberInput, EmailInput

from .models import Representante

class RepresentanteForm(forms.ModelForm):
    # constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        this_year = datetime.now().year
        years = range(this_year - 80, this_year - 14)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

            self.fields['nombres'].widget = TextInput(
                attrs={'placeholder': 'Ingrese sus dos nombres', 'class': 'form-control form-rounded'})
            self.fields['apellidos'].widget = TextInput(
                attrs={'placeholder': 'Ingrese sus dos Apellidos', 'class': 'form-control form-rounded'})
            self.fields['cedula'].widget = TextInput(
                attrs={'placeholder': 'Ingrese numero de cedula', 'class': 'form-control form-rounded'})
            self.fields['correo'].widget = EmailInput(attrs={'placeholder': 'abc@correo.com',
                                                             'class': 'form-control form-rounded'})
            self.fields['sexo'].widget.attrs['class'] = 'selectpicker selectWrapper'
            self.fields["fecha_nacimiento"].widget = SelectDateWidget(years=years, attrs={'class': 'selectpicker'})
        # habilitar, desabilitar, y mas

    class Meta:
        model = Representante
        fields = ['nombres',
                  'apellidos',
                  'cedula',
                  'correo',
                  'sexo',
                  'fecha_nacimiento'
                  ]
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'cedula': 'N° de cedula',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'correo': 'Correo',
            'sexo': 'Genero',
        }
        widgets = {
            'nombres': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'cedula': forms.TextInput(),
            'sexo': forms.Select(attrs={'class': 'selectpicker','data-width': 'fit'}),
 #           'fecha_nacimiento': forms.extras.SelectDateWidget(),
            'correo': forms.EmailInput(),
        }

