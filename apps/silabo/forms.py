from django.forms import *
from .models import Materia, Silabo
from django import forms
class SilaboForm(forms.Form):
        materia = forms.ModelChoiceField(
            label=u'Materia',
            queryset=Materia.objects.all(),
            widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-width': 'auto'})
        )

class SilaboForm2(forms.Form):
    materia = forms.ModelChoiceField(
        label=u'Materia',
        queryset=Materia.objects.all(),
        widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-width': 'auto'})
    )


class SilaboFormEdit(forms.ModelForm):
    #constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        #habilitar, desabilitar, y mas

    class Meta:
        model = Silabo
        fields = ['unidad',
                  'semana',
                  'clase',
                  'tema',
                  ]
        labels = {
            'unidad': 'Unidad',
            'semana': 'Semana',
            'clase': 'Clase',
            'tema': 'Tema',
        }
        widgets = {
            'unidad': forms.NumberInput(),
            'semana':   forms.NumberInput(),
            'clase': forms.NumberInput(),
            'tema': forms.Textarea(),
        }

