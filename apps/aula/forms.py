from django.forms import *
from .models import Aula

class AulaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero'].widget.attrs['autofocus'] = True

    class Meta:
        model = Aula
        fields = 'numero',
        labels = {
            'numero': 'Numero',
        }
        widgets = {
            'numero': TextInput(attrs={'placeholder': 'Ingrese un numero', 'class': 'form-control form rounded',
                                       'style': 'width: 50%; '}),
        }



    id = IntegerField(widget=HiddenInput(attrs={'id': 'id'}), initial=0)