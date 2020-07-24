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

    def clean(self, *args, **kwargs):
        cleaned_data = super(PeriodoForm, self).clean(*args, **kwargs)
        periodo_inicio = cleaned_data.get('periodo_inicio', None)
        periodo_fin = cleaned_data.get('periodo_fin', None)
        if periodo_inicio is not None:
            for row2 in Periodo.objects.raw('SELECT "count"(*) as id FROM periodo WHERE %s BETWEEN periodo_inicio and periodo_fin', [periodo_inicio]):
                if row2.id > 0:
                    self.add_error('periodo_inicio', 'Periodo ya existente con este rango de fechas')
                else:
                    if periodo_fin <= periodo_inicio:
                        self.add_error('periodo_inicio', 'No puede ingresar el final mayor que el inicio')

