from django.shortcuts import render, redirect
from .models import *
from apps.representante.models import *
from django.urls import reverse_lazy
from django.views.generic import *
import json
from django.http import HttpResponse
from apps.representante.forms import RepresentanteForm
from django.http import HttpResponseRedirect


opc_icono = 'fa fa-group'
opc_ruta = '/representante/'
opc_nuevo = '/representante/nuevo'
opc_crud = '/representante/crear/'
opc_delete = '/representante/borrar'
opc_entidad = 'Representantes'



def nuevo(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Representante', 'action': 'add', 'titulo': 'Nuevo Registro de un Representante',
    }
    if request.method == 'GET':
        data['form'] = RepresentanteForm()
    return render(request, 'back-end/representante/representante_form.html', data)

def crear(request):
    f = RepresentanteForm(request.POST)
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud
    }
    action = request.POST['action']
    data['action'] = action
    if request.method == 'POST' and 'action' in request.POST:
        if action == 'add':
            f = RepresentanteForm(request.POST)
            if f.is_valid():
                f.save()
            else:
                data = {
                    'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
                    'boton': 'Guardar Representante', 'action': 'add', 'titulo': 'Nuevo Registro de un Representante',
                    'form': f
                }
                return render(request, 'back-end/representante/representante_form.html', data)
            return HttpResponseRedirect('/alumnos/nuevo')

def listado(request):
    lista= Representante.objects.all()
    contexto={"lista":lista}
    return render(request, 'back-end/representante/representante_list.html', contexto)

def editar(request, id_representante):
    representante = Representante.objects.get(id=id_representante)
    opc_edit = '/representante/editar/' + id_representante + '/'

    if request.method == 'GET':
        form = RepresentanteForm(instance=representante)
    else:
        form = RepresentanteForm(request.POST, instance=representante)
        if form.is_valid():
            form.save()
        return redirect('representante:lista')
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_edit, 'entidad': opc_entidad,
        'boton': 'Guardar Representante', 'titulo': 'Editar Registro de un Representante',
        'form': form
    }

    return render(request, 'back-end/representante/representante_form.html', data)
