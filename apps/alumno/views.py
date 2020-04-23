from django.shortcuts import render, redirect
from apps.lista.models import *
from django.views.generic import *
from django.http import HttpResponse
from apps.alumno.forms import AlumnoForm
from django.http import HttpResponseRedirect
import json
from django.db.models import Q

opc_icono = 'fa fa-odnoklassniki'
opc_ruta = '/alumnos/'
opc_nuevo = '/alumnos/nuevo'
opc_crud = '/alumnos/crear/'
opc_delete = '/alumnos/borrar'
opc_entidad = 'Alumnos'


def nuevo(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Alumno', 'action': 'add', 'titulo': 'Nuevo Registro de un Alumno',
    }
    if request.method == 'GET':
        data['form'] = AlumnoForm()
    return render(request, 'back-end/alumno/alumno_form.html', data)

def crear(request):
    f = AlumnoForm(request.POST)
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud
    }
    action = request.POST['action']
    data['action'] = action
    if request.method == 'POST' and 'action' in request.POST:
        if action == 'add':
            f = AlumnoForm(request.POST)
            if f.is_valid():
                f.save()
            else:
                data = {
                    'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
                    'boton': 'Guardar Alumno', 'action': 'add', 'titulo': 'Nuevo Registro de un Alumno',
                    'form': f
                }
                return render(request, 'back-end/alumno/alumno_form.html', data)
            return HttpResponseRedirect('/alumnos/listado')

def editar(request, id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)
    opc_edit = '/alumnos/editar/' + id_alumno + '/'

    if request.method == 'GET':
        form = AlumnoForm(instance=alumno)
    else:
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
        return redirect('alumnos:lista')
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_edit, 'entidad': opc_entidad,
        'boton': 'Guardar Alumno', 'titulo': 'Editar Registro de un Alumno',
        'form': form
    }

    return render(request, 'back-end/alumno/alumno_form.html', data)

def estado(request):
    data = {}
    if request.method == 'POST':
        try:
            fecha_hoy = date.today()
            ano = fecha_hoy.year + 1
            h = Alumno.objects.get(pk=request.POST['id'])
            h.estado = request.POST['estado']
            h.save()
            r = int(request.POST['estado'])
            if r == 1:
                m = Listado.objects.get(
                    Q(periodo__periodo_fin__year=fecha_hoy.year) | Q(periodo__periodo_fin__year=ano),
                    alumno=request.POST['id'], estado=2)
                m.estado = 0
                m.save()
            if r == 1:
                m = Listado.objects.get(
                    Q(periodo__periodo_fin__year=fecha_hoy.year) | Q(periodo__periodo_fin__year=ano),
                    Q(estado=0) | Q(estado=2), alumno=request.POST['id'])
                m.estado = 1
                m.save()
            if r == 2:
                m = Listado.objects.get(
                    Q(periodo__periodo_fin__year=fecha_hoy.year) | Q(periodo__periodo_fin__year=ano),
                    alumno=request.POST['id'], estado=0)
                m.estado = 2
                m.save()
            data['resp'] = True
        except Exception as e:
            data['error'] = e.message
            data['resp'] = False
    return HttpResponse(json.dumps(data), content_type="application/json")



class Alumno_lista(ListView):
    model = Alumno
    template_name = 'back-end/alumno/alumno_list.html'

