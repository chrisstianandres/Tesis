from django.views.generic import *
from django.shortcuts import *
from apps.aula.forms import *
from apps.asignar.models import *
from apps.aula.models import *
import json
from django.http import HttpResponseRedirect
#---------------------------
opc_icono = 'fa fa-sort-alpha-des'
opc_ruta = '/aula/'
opc_nuevo = '/aula/nuevo'
opc_crud = '/aula/crear'
opc_delete = '/aula/borrar'
opc_entidad = 'Aulas'

#---------------------------

def nuevo(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Aula', 'action': 'add', 'titulo': 'Nuevo Registro de un Aula'
    }
    if request.method == 'GET':
        data['form'] = AulaForm()
    return render(request, 'back-end/aula/aula_form.html', data)

def crear(request):
    f = AulaForm(request.POST)
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Aula', 'action': 'add', 'titulo': 'Nuevo Registro de un Aula'
    }
    action = request.POST['action']
    data['action'] = action
    if request.method == 'POST' and 'action' in request.POST:
            if action == 'add':
                f = AulaForm(request.POST)
            if f.is_valid():
                f.save()
            else:
                data['form'] = f
                return render(request, 'back-end/aula/aula_form.html', data)
            return HttpResponseRedirect('/aula/listado')

def aula_list(request):
    lista = Aula.objects.all()
    contexto = {'lista': lista}
    return render(request, 'back-end/aula/aula_list.html', contexto)

def editar(request, id_aula):

    aula = Aula.objects.get(id=id_aula)
    opc_edit = '/aula/editar/'+id_aula+'/'

    if request.method == 'GET':
        form = AulaForm(instance=aula)
    else:
        form = AulaForm(request.POST, instance=aula)
        if form.is_valid():
            form.save()
        return redirect('/aula/listado')
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_edit, 'entidad': opc_entidad,
        'boton': 'Guardar Aula',  'titulo': 'Editar Registro de un Aula',
        'form': form
    }
    return render(request, 'back-end/aula/aula_form.html', data)

def eliminar(request):
    data = {}
    if request.method == 'POST':
        try:
            h = Aula.objects.get(pk=request.POST['id'])
            h.delete()
            data['resp'] = True
        except Exception as e:
            data['error'] = e.message
            data['resp'] = False
    return HttpResponse(json.dumps(data), content_type="application/json")