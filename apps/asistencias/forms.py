from django import forms
from bootstrap_datepicker_plus import *
from .models import *
from apps.parcial.models import *
from apps.quimestre.models import *

class AsistenciasForm(forms.Form):
    periodo = forms.ModelChoiceField(
        label=u'Periodo',
        queryset=Periodo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-rounded'})
    )
    materia = forms.ModelChoiceField(
        label=u'Materia',
        queryset=Materia.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control form-rounded'})
    )
    curso = forms.ModelChoiceField(
        label=u'Curso',
        queryset=Curso.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control form-rounded'})
    )
    desde = forms.TimeField(widget=DatePickerInput(
                options={
                    "format": "YYYY-MM-DD",
                    "locale": "es",
                    "startDate": '-3d',
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True
                }
            ), label=u'Desde',)


    hasta = forms.TimeField(widget=DatePickerInput(
                options={
                    "format": "YYYY-MM-DD",
                    "locale": "es",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True
                }
            ), label=u'Hasta',)
