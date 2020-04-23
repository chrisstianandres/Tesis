from django import forms

from .models import Periodo, Asignar, Listado
from apps.parcial.models import *
from apps.quimestre.models import *

class PeriodoForm(forms.Form):
    periodo = forms.ModelChoiceField(
        label=u'Periodo',
        queryset=Periodo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-rounded'})
    )
    materia = forms.ModelChoiceField(
        label=u'Materia',
        queryset=Asignar.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control form-rounded'})
    )
    curso = forms.ModelChoiceField(
        label=u'Curso',
        queryset=Listado.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control form-rounded'})
    )
    quimestre = forms.ModelChoiceField(
        label=u'Quimestre',
        queryset=Quimestre.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-rounded'})
    )
    parcial = forms.ModelChoiceField(
        label=u'Parcial',
        queryset=Parcial.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control form-rounded'})
    )


def __init__(self, *args, **kwargs):
        super(PeriodoForm, self).__init__(*args, **kwargs)
        self.fields['materia'].queryset = Asignar.objects.none()
        self.fields['curso'].queryset = Listado.objects.none()
