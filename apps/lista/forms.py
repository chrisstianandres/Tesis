from django import forms
from datetime import *
# from django.forms.extras.widgets import SelectDateWidget
# from django.contrib.admin import widgets
# from bootstrap_datepicker_plus import DatePickerInput
from django.forms import SelectDateWidget, TextInput

from .models import Listado
from apps.periodo.models import Periodo


class ListadoForm(forms.ModelForm):
    # constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        year = datetime.today().year
        query = Periodo.objects.filter(periodo_inicio__year=year)
       #value = "%s" > % s < / option > ' % (
        #periodo.periodo_id,
        #periodo.periodo)


        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'

            })
            self.fields['alumno'].widget.attrs['class'] = 'selectpicker'
            self.fields['periodo'].widget.attrs['class'] = 'selectpicker'
            self.fields['periodo'].queryset = Periodo.objects.filter(periodo_inicio__year=year)
            self.initial['periodo'] = Periodo.objects.get(periodo_inicio__year=year)
            self.fields['curso'].widget.attrs['class'] = 'selectpicker'
        # habilitar, desabilitar, y mas

    class Meta:
        model = Listado
        fields = [
            'periodo',
            'alumno',

            'curso',
        ]
        labels = {
            'alumno': 'Alumno',
            'periodo': 'Periodo',
            'curso': 'Curso',
        }
        widgets = {
            'alumno': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-width': '75%'}),
            'periodo': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-width': '75%'}),
            'curso': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-width': '75%'}),
        }
