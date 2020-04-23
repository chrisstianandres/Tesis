# -*- coding: utf-8 -*-
from django.shortcuts import *
from .models import *
from django.views.generic import *
from apps.horario.forms import *
from django.http import *
from apps.silabo.models import Silabo
import json
import datetime
from django.db.models import Count

# ---------------------------
opc_icono = 'fa fa-calendar-plus-o'
opc_ruta = '/horario/'
opc_entidad = 'Horario'
opc_nuevo = '/horario/nuevo/'
opc_crud = '/horario/crear'
opc_delete = '/horario/borrar/'


# ---------------------------
def horario_list(request):
    data = {
        'titulo': 'Listado de Horario'
    }
    return render(request, 'back-end/horario/horario_list.html', data)

def horario_list_admin(request):
    data = {
        'titulo': 'Listado de Horario de los docentes'
    }
    return render(request, 'back-end/horario/horario_list_admin.html', data)

def nuevo_admin(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Horario', 'action': 'add', 'titulo': 'Nuevo Registro de Horario'
    }
    if request.method == 'GET':
        data['form'] = HorarioForm()
    return render(request, 'back-end/horario/HorarioForm.html', data)

def editar(request, id):
    horario = Horario.objects.get(id=id)
    opc_edit = '/horario/editar_admin/' + id + '/'
    if request.method == 'GET':
        form = HorarioForm_edit(instance=horario)
    else:
        form = HorarioForm_edit(request.POST, instance=horario)
        if form.is_valid():
            form.save()
        return redirect("horario:horarios_admin")
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_edit, 'entidad': 'Horario / Admin',
        'boton': 'Guardar Horario',  'titulo': 'Editar Registro',
        'form': form
    }

    return render(request, 'back-end/horario/Horarioform_edit.html', data)


def nuevo(request):
    a = request.user.id
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Horario', 'action': 'add', 'titulo': 'Nuevo Registro de Horario'
    }
    if request.method == 'GET':
        data['form'] = HorarioForm2()
    return render(request, 'back-end/horario/HorarioForm2.html', data)


def get_periodo(request):
    docente_id = request.POST['docente_id']
    periodos = Asignar.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if docente_id:
        periodos = Asignar.objects.filter(docente_id=docente_id).distinct("periodo_id")
        for p in periodos:
            options += '<option value="%s">%s</option>' % (p.periodo_id, p.periodo)
        response = {}
        response['periodos'] = options
        return JsonResponse(response)


def get_materia(request):
    periodo_id = request.POST['periodo_id']
    docente_id = request.POST['docente_id']
    materias = Asignar.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if periodo_id:
        materias = Asignar.objects.filter(periodo=periodo_id, docente_id=docente_id).distinct("materia")
    for materia in materias:
        options += '<option value="%s">%s</option>' % (
            materia.materia.id,
            materia.materia
        )
    response = {}
    response['materias'] = options
    return JsonResponse(response)


def get_curso(request):
    materia_id = request.POST['materia_id']
    periodo_id = request.POST['periodo_id']
    docente_id = request.POST['docente_id']
    cursos = Asignar.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if materia_id:
        cursos = Asignar.objects.filter(materia=materia_id, periodo=periodo_id, docente=docente_id).distinct("curso_id")
        print("hola")
    for curso in cursos:
        options += '<option value="%s">%s</option>' % (
            curso.id,
            curso.curso
        )
    response = {}
    response['cursos'] = options
    return JsonResponse(response)


def get_silabo(request):
    materia_id = request.POST['materia_id']
    silabos = Silabo.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if materia_id:
        silabos = Silabo.objects.filter(materia=materia_id).order_by("clase")
    for silabo in silabos:
        options += '<option value="%s">%s</option>' % (
            silabo.id,
            silabo.tema
        )
    response = {}
    response['silabos'] = options
    return JsonResponse(response)


def get_alumno(request):
    id = request.POST['id']
    h = Horario.objects.get(id=id)
    p = h.asignar.periodo.id
    c = h.asignar.curso.id
    a = h.asignar.docente.id
    if id:
        data = [[alumno.id, alumno.alumno.apellidos + " " + alumno.alumno.nombres, alumno.id, h.id]
                for alumno in Listado.objects.filter(periodo=p, curso=c, alumno__estado=0,
                                                     periodo__asignar__docente_id=a).order_by("alumno_id").distinct("alumno_id")]
        a = Listado.objects.filter(periodo=p, curso=c, alumno__estado=0, periodo__asignar__docente_id=a)
        print(a.query)
        return HttpResponse(json.dumps(data), content_type="application/json")


def save_horario(request):
    data = {}
    if request.method == 'POST':
        datos = json.loads(request.POST['datos'])
        for sub in datos:
            f = sub['fecha']
            str(f)
            d = sub['desde']
            str(d)
            h = sub['hasta']
            str(h)
            s = sub['silabo']
            str(s)
            if f == "" or d == "" or h == "" or s == "":
                data['error'] = "Existe un campo vacio por favor completalo y vuelve a intentarlo"
                data['resp'] = False
            else:

                f = sub['fecha']
                str(f)
                d = sub['desde']
                str(d)
                h = sub['hasta']
                str(h)
                s = sub['silabo']
                int(s)
                a = sub['asignar']
                p = sub['docente']
                int(p)
                i = "'1 min'"

                if Horario.objects.filter(asignar=a, silabo=s, hora_inicio=d, hora_fin=h, fecha=f):
                    data['error'] = "Ya existe un tema igual registrado"
                    data['resp'] = False
                else:
                    for row in Horario.objects.raw(
                            'SELECT "count"(*) as id FROM horario INNER JOIN asignar ON horario.asignar_id = asignar."id" '
                            'WHERE %s BETWEEN horario.hora_inicio AND hora_fin::TIME - %s::INTERVAL and '
                            'asignar.docente_id=%s and horario.fecha= %s', [d, i, p, f]):
                        if row.id == 1:
                            data[
                                'error'] = "El Docente tiene actividades ya asignadas  en algun/nos de los " \
                                           "rangos de horas ingresados <br> Verificalos en el horario " \
                                           "y vuelve a intentarlo "
                            data['resp'] = False
                        else:
                            n = Horario()
                            n.asignar_id = a
                            n.silabo_id = s
                            n.fecha = f
                            n.hora_inicio = d
                            n.hora_fin = h
                            n.save()
                            data['resp'] = True
        return HttpResponse(json.dumps(data), content_type="application/json")


def get_periodo_2(request):
    periodos = Asignar.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    periodos = Asignar.objects.filter(docente_id=request.user.id).distinct("periodo_id")
    for p in periodos:
        options += '<option value="%s">%s</option>' % (p.periodo_id, p.periodo)
        response = {}
        response['periodos'] = options
        return JsonResponse(response)


def get_materia_2(request):
    periodo_id = request.POST['periodo_id']
    docente_id = request.user.id
    materias = Asignar.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if periodo_id:
        materias = Asignar.objects.filter(periodo=periodo_id, docente_id=docente_id).distinct("materia")
    for materia in materias:
        options += '<option value="%s">%s</option>' % (
            materia.materia.id,
            materia.materia
        )
    response = {}
    response['materias'] = options
    return JsonResponse(response)


def get_curso_2(request):
    materia_id = request.POST['materia_id']
    periodo_id = request.POST['periodo_id']
    cursos = Asignar.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if materia_id:
        cursos = Asignar.objects.filter(materia=materia_id, periodo=periodo_id, docente_id=request.user.id)
    for curso in cursos:
        options += '<option value="%s">%s</option>' % (
            curso.id,
            curso.curso
        )
    response = {}
    response['cursos'] = options
    return JsonResponse(response)


def save_horario_2(request):
    data = {}
    if request.method == 'POST':
        datos = json.loads(request.POST['datos'])
        for sub in datos:
            f = sub['fecha']
            str(f)
            d = sub['desde']
            str(d)
            h = sub['hasta']
            str(h)
            s = sub['silabo']
            str(s)
            if f == "" or d == "" or h == "" or s == "":
                data['error'] = "Existe un campo vacio por favor completalo y vuelve a intentarlo"
                data['resp'] = False
            else:

                f = sub['fecha']
                str(f)
                d = sub['desde']
                str(d)
                h = sub['hasta']
                str(h)
                s = sub['silabo']
                int(s)
                a = sub['asignar']
                p = request.user.id
                int(p)
                i = "'1 min'"

                if Horario.objects.filter(asignar=a, silabo=s, hora_inicio=d, hora_fin=h, fecha=f):
                    data['error'] = "Ya existe un tema igual registrado"
                    data['resp'] = False
                else:
                    for row in Horario.objects.raw(
                            'SELECT "count"(*) as id FROM horario INNER JOIN asignar ON horario.asignar_id = asignar."id" '
                            'WHERE %s BETWEEN horario.hora_inicio AND hora_fin::TIME - %s::INTERVAL and '
                            'asignar.docente_id=%s and horario.fecha= %s', [d, i, p, f]):
                        if row.id == 1:
                            data[
                                'error'] = "El Docente tiene actividades ya asignadas  en algun/nos de los rangos de horas ingresados <br> Verificalos en el horario y vuelve a intentarlo "
                            data['resp'] = False
                        else:
                            n = Horario()
                            n.asignar_id = a
                            n.silabo_id = s
                            n.fecha = f
                            n.hora_inicio = d
                            n.hora_fin = h
                            n.save()
                            data['resp'] = True
        return HttpResponse(json.dumps(data), content_type="application/json")
