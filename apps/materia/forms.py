from django.forms import *
from .models import Materia

class MateriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Materia
        fields = 'nombre',
        labels = {
            'nombre': 'Nombre',
        }
        widgets = {
            'nombre': TextInput(attrs={'placeholder': 'Ingrese un nombre', 'class': 'form-control', 'style': 'width: 50%; '}),
        }



    id = IntegerField(widget=HiddenInput(attrs={'id': 'id'}), initial=0)