# Create your views here.
# -*- coding: utf-8 -*-
from .forms import *
from django.http import *
from django.shortcuts import *
from .models import *
from apps.asignar.models import *
from apps.curso.forms import *
import json
#---------------------------
opc_menu = '/curso/curso_menu'
opc_icono = 'fa fa-archive'
opc_ruta = '/curso/'
opc_nuevo = '/curso/nuevo'
opc_crud = '/curso/crear'
opc_delete = '/curso/borrar'
opc_entidad = 'Curso'
#---------------------------
def curso_list(request, id_materia, id_periodo):
    listacurso = Asignar.objects.filter(docente_id=request.user.id, materia_id=id_materia,
                                        periodo_id=id_periodo).distinct("curso_id")
    contexto = {'listacurso': listacurso}
    return render(request, "back-end/curso/cursoindex.html", contexto)

def curso_list_materias(request):
    curso = request.POST["curso"]
    listamaterias = Asignar.objects.filter(docente_id=request.user.id, curso_id=curso).distinct("materia_id")
    contexto = {'listamaterias': listamaterias}
    return render(request, "back-end/curso/cursoindex.html", contexto)

def asistencia_list(request):
    a = request.user.id
    listaasistencia = Curso.objects.raw('SELECT curso.nombre,  max(horario."id") as id FROM horario INNER JOIN curso ON horario.curso_id = curso."id" INNER JOIN aula ON curso.aula_id = aula."id" INNER JOIN "public".docente ON "public".horario.docente_id = "public".docente.user_ptr_id INNER JOIN "public".auth_user ON "public".docente.user_ptr_id = "public".auth_user."id" WHERE docente.user_ptr_id =%s GROUP BY curso.nombre',[ a ])
    contexto = {'listacurso': listaasistencia}
    return render(request, "back-end/curso/asistenciaindex.html",contexto)

def nuevo_curso(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Curso', 'action': 'add', 'titulo': 'Nuevo Registro de Curso',
    }
    if request.method == 'GET':
        data['form'] = CursoForm()
    return render(request, 'back-end/curso/curso_form.html', data)

def crear_curso(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud
    }
    action = request.POST['action']
    data['action'] = action
    if request.method == 'POST' and 'action' in request.POST:
        if action == 'add' or action == 'edit':
            if action == 'add':
                f = CursoForm(request.POST)
            elif action == 'edit':
                f = CursoForm(request.POST, instance=Curso.objects.get(id=request.POST['id']))
            if f.is_valid():
                f.save()
            else:
                data['form'] = f
                return render(request, 'back-end/curso/curso_form.html', data)
            return HttpResponseRedirect('/curso/')

def lista(request):
    lista = Curso.objects.all()
    contexto = {'lista': lista}
    return render(request, "back-end/curso/curso_lista.html", contexto)

def editar(request, id_curso):
    curso=Curso.objects.get(id=id_curso)
    opc_edit = '/curso/editar/' + id_curso + '/'

    if request.method == 'GET':
        form = CursoForm(instance=curso)
    else:
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
        return redirect('curso:lista')
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_edit, 'entidad': opc_entidad,
        'boton': 'Guardar Curso', 'titulo': 'Editar Registro de un Curso',
        'form': form
    }

    return render(request, 'back-end/curso/curso_form.html', data)

def eliminar(request):
    data = {}
    if request.method == 'POST':
        try:
            h = Curso.objects.get(pk=request.POST['id'])
            h.delete()
            data['resp'] = True
        except Exception as e:
            data['error'] = e.message
            data['resp'] = False
    return HttpResponse(json.dumps(data), content_type="application/json")




