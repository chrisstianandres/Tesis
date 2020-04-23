from django.shortcuts import render, redirect
from apps.lista.models import *
from django.views.generic import *
from django.http import HttpResponse
from apps.periodo.forms import *
from django.http import HttpResponseRedirect
import json
from django.db.models import Q

opc_icono = 'fa fa-clock-o'
opc_ruta = '/periodo/'
opc_nuevo = '/periodo/nuevo'
opc_crud = '/periodo/crear/'
opc_delete = '/periodo/borrar'
opc_entidad = 'Periodos'


def nuevo(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Periodo', 'action': 'add', 'titulo': 'Nuevo Registro de un Periodo',
    }
    if request.method == 'GET':
        data['form'] = PeriodoForm()
    return render(request, 'back-end/periodo/periodo_form.html', data)

def crear(request):
    f = PeriodoForm(request.POST)
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud
    }
    action = request.POST['action']
    data['action'] = action
    if request.method == 'POST' and 'action' in request.POST:
        if action == 'add':
            f = PeriodoForm(request.POST)
            if f.is_valid():
                f.save()
            else:
                data = {
                    'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
                    'boton': 'Guardar Periodo', 'action': 'add', 'titulo': 'Nuevo Registro de un Periodo',
                    'form': f
                }
                return render(request, 'back-end/periodo/periodo_form.html', data)
            return HttpResponseRedirect('/periodo/listado')

def listado (request):
    lista= Periodo.objects.all()
    contexto={"lista":lista}
    return render(request, 'back-end/periodo/periodo_list.html', contexto)

def editar(request, id_periodo):
    periodo = Periodo.objects.get(id=id_periodo)
    opc_edit = '/periodo/editar/' + id_periodo + '/'

    if request.method == 'GET':
        form = PeriodoForm(instance=periodo)
    else:
        form = PeriodoForm(request.POST, instance=periodo)
        if form.is_valid():
            form.save()
        return redirect('periodo:listado')
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_edit, 'entidad': opc_entidad,
        'boton': 'Guardar Periodo', 'titulo': 'Editar Registro de un Periodo',
        'form': form
    }
    return render(request, 'back-end/periodo/periodo_form.html', data)

def eliminar(request):
    data = {}
    if request.method == 'POST':
        try:
            h = Periodo.objects.get(pk=request.POST['id'])
            h.delete()
            data['resp'] = True
        except Exception as e:
            data['error'] = e.message
            data['resp'] = False
    return HttpResponse(json.dumps(data), content_type="application/json")