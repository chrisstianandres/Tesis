from django import forms
from datetime import *
#from django.forms import extras
from django.forms import SelectDateWidget, TextInput, NumberInput, EmailInput

from .models import Periodo

class PeriodoForm(forms.ModelForm):
    # constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        this_year = datetime.now().year
        years = range(this_year, this_year + 15)
        yearsf = range(this_year + 1, this_year + 15)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

            self.fields["periodo_inicio"].widget = SelectDateWidget(years=years,
                                                                      attrs={'class': 'selectpicker'})
            self.fields["periodo_fin"].widget = SelectDateWidget(years=yearsf,
                                                                      attrs={'class': 'selectpicker'})
        # habilitar, desabilitar, y mas

    class Meta:
        model = Periodo
        fields = ['periodo_inicio',
                  'periodo_fin'
                  ]
        labels = {
            'periodo_inicio': 'Desde:',
            'periodo_fin': 'Hasta:'
        }
        widgets = {
            'periodo_inicio': forms.TextInput(),
            'periodo_fin': forms.TextInput(),
            'cedula': forms.TextInput(),
        }

