from bootstrap_datepicker_plus import *
from django import forms
from .models import Horario
from .models import Docente
from .models import Materia
from .models import Curso
from .models import Silabo
from .models import Periodo

class HorarioForm(forms.Form):
    periodo = forms.ModelChoiceField(
        label=u'Periodo',
        queryset=Periodo.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control form-rounded'})
    )
    docente = forms.ModelChoiceField(
        label=u'Docente',
        queryset=Docente.objects.all(),
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

    clase = forms.ModelChoiceField(
        label=u'Clase',
        queryset=Silabo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-rounded'})
    )

    desde = forms.TimeField(widget=TimePickerInput(),)
    hasta = forms.TimeField(widget=TimePickerInput(), )
    fecha = forms.TimeField(widget=DatePickerInput(
                options={
                    "format": "DD/MM/YYYY",
                    "locale": "es",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True
                }
            ),)

class HorarioForm2(forms.Form):
    periodo = forms.ModelChoiceField(
        label=u'Periodo',
        queryset=Periodo.objects.none(),
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

    clase = forms.ModelChoiceField(
        label=u'Clase',
        queryset=Silabo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-rounded'})
    )

    desde = forms.TimeField(widget=TimePickerInput(),)
    hasta = forms.TimeField(widget=TimePickerInput(), )
    fecha = forms.TimeField(widget=DatePickerInput(
                options={
                    "format": "DD/MM/YYYY",
                    "locale": "es",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True
                }
            ),)

class HorarioForm_edit(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['hora_inicio',
                  'hora_fin',
                  'asignar',
                  'silabo',
                  'fecha',
                  ]
        labels = {
            'hora_inicio': 'Desde',
            'hora_fin': 'Hasta',
            'asignar': 'Docente',
            'silabo': 'Tema',
            'fecha': 'Fecha',
        }
        widgets = {
            'hora_inicio': TimePickerInput(),
            'hora_fin': TimePickerInput,
            'asignar': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-width': 'auto'}),
            'silabo': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-width': 'auto'}),
            'fecha': DatePickerInput(
                options={
                    "format": "DD/MM/YYYY",
                    "locale": "es",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True
                }
            )
        }




