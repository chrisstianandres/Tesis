from django.shortcuts import render
import json

from apps.notas.models import *
from apps.periodo.models import *
#from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from apps.asignar.models import *
from apps.lista.models import *
from .forms import *

def vista_notas_request(request):
    form = PeriodoForm()
    if request.method == 'POST':
        form = PeriodoForm(request.POST)
    return render(request, 'back-end/notas/notasindex_alumnos.html', {'form': form})

def vista_notas(request):
    form = PeriodoForm()
    if request.method == 'POST':
        form = PeriodoForm(request.POST)
    return render(request, 'back-end/notas/notas_form_report.html', {'form': form})