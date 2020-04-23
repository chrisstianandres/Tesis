from django import forms
from django.forms import SelectDateWidget, TextInput, NumberInput
from .models import Curso


class CursoForm(forms.ModelForm):
    #constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['aula'].widget.attrs['class'] = 'selectpicker'
            self.fields['nombre'].widget = TextInput(attrs={'class': 'form-control form-rounded',
                                                             'style': 'width: 50%; display: inline-block;'})
        #habilitar, desabilitar, y mas

    class Meta:
        model = Curso
        fields = 'nombre', \
                 'aula',
        # exclude = ['materia']
        widgets = {

            'aula': forms.Select(
                    attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-size': '20'}),
        }
