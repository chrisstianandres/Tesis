from django import forms
from datetime import *
#from django.forms.extras.widgets import SelectDateWidget
#from django.contrib.admin import widgets
#from bootstrap_datepicker_plus import DatePickerInput
from django.forms import SelectDateWidget, TextInput

from .models import Asignar


class AsignarForm(forms.ModelForm):
    #constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['docente'].widget.attrs['class'] = 'selectpicker'
            self.fields['materia'].widget.attrs['class'] = 'selectpicker'
            self.fields["periodo"].widget.attrs['class'] = 'selectpicker'
            self.fields["curso"].widget.attrs['class'] = 'selectpicker'
        #habilitar, desabilitar, y mas

    class Meta:
        model = Asignar
        fields = ['docente',
                  'materia',
                  'periodo',
                  'curso',
                  ]
        labels = {
            'docente': 'Docente',
            'materia': 'Materia',
            'periodo': 'Periodo',
            'curso'  : 'Curso',
        }
        widgets = {
            'docente': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-width': 'auto'}),
            'materia': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-width': 'auto'}),
            'periodo': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-width': 'auto'}),
            'curso':   forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-width': 'auto'}),
        }



