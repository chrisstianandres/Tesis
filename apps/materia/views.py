
# -*- coding: utf-8 -*-
from django.views.generic import *
from django.shortcuts import *
from apps.materia.forms import *
from apps.asignar.models import *
from apps.silabo.models import *
from django.http import HttpResponseRedirect
#---------------------------

#---------------------------
class Materia_list (ListView):
    model = Materia
    template_name = 'back-end/materia/materia_list.html'


opc_icono = 'fa fa-book'
opc_ruta = '/materias/'
opc_nuevo = '/materia/nuevo'
opc_crud = '/materia/crear'
opc_delete = '/materia/borrar'
opc_entidad = 'Materias'


def nuevo(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Materia', 'action': 'add', 'titulo': 'Nuevo Registro de una Materia'
    }
    if request.method == 'GET':
        data['form'] = MateriaForm()
    return render(request, 'back-end/materia/materia_form.html', data)

def crear(request):
    f = MateriaForm(request.POST)
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Materia', 'action': 'add', 'titulo': 'Nuevo Registro de una Materia'
    }
    action = request.POST['action']
    data['action'] = action
    if request.method == 'POST' and 'action' in request.POST:
            if action == 'add':
                f = MateriaForm(request.POST)
            if f.is_valid():
                f.save()
            else:
                data['form'] = f
                return render(request, 'back-end/materia/materia_form.html', data)
            return HttpResponseRedirect('/materia/listado')

def materia_list(request):
    a = request.user.id
    listamateria = Materia.objects.all()
    contexto = {'listamateria': listamateria}
    return render(request, 'back-end/materia/materia_list.html', contexto)

def silabo(request, id_materia):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Materia', 'action': 'add', 'titulo': 'Nuevo Registro de una Materia'
    }
    silabos = Silabo.objects.filter(materia_id=id_materia)
    contexto = {'silabos': silabos, 'data': data}
    return render(request, "back-end/silabo/silabo_general.html", contexto)





def editar(request, id_materia):

    materia = Materia.objects.get(id=id_materia)
    opc_edit = '/materias/editar/'+id_materia+'/'

    if request.method == 'GET':
        form = MateriaForm(instance=materia)
    else:
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
        return redirect('materias:listado')
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_edit, 'entidad': opc_entidad,
        'boton': 'Guardar Materia',  'titulo': 'Editar Registro de una Materia',
        'form': form
    }

    return render(request, 'back-end/materia/materia_form.html', data)