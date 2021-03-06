from django.shortcuts import render, redirect
from .models import *
from apps.asignar.models import *
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import HttpResponse
from apps.asignar.forms import AsignarForm
from django.http import *
import json
from django.views.decorators.csrf import csrf_exempt

opc_icono = 'fa fa-briefcase'
opc_ruta = '/asignar/'
opc_nuevo = '/asignar/nuevo'
opc_crud = '/asignar/crear/'
opc_delete = '/asignar/borrar'
opc_entidad = 'Asignaciones'


def nuevo(request, id_docente):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Asignacion', 'action': 'add', 'titulo': 'Nueva Asignacion de una Materia',
        'id_docente': id_docente,
    }

    return render(request, 'back-end/asignar/asignar_form.html', data)


def get_datos(request):
    k = " - "
    year = datetime.today().year
    periodos = Periodo.objects.filter(periodo_inicio__year=year)
    materias = Materia.objects.all().order_by("nombre")
    cursos = Curso.objects.all().order_by("nombre")
    optionsp = ''
    optionsm = '<option value="" selected="selected">---------</option>'
    optionsc = '<option value="" selected="selected">---------</option>'
    for periodo in periodos:
        i = str(periodo.periodo_inicio.year)
        f = str(periodo.periodo_fin.year)
        optionsp += '<option value="%s">%s</option>' % (
            periodo.id,
            i + k + f,
        )
    for materia in materias:
        optionsm += '<option value="%s">%s</option>' % (
            materia.id,
            materia.nombre,
        )
    for curso in cursos:
        optionsc += '<option value="%s">%s  %s</option>' % (
            curso.id,
            curso.nombre,
            curso.get_seccion_display()
        )
    response = {}
    response['periodos'] = optionsp
    response['materias'] = optionsm
    response['cursos'] = optionsc
    return JsonResponse(response)


@csrf_exempt
def crear(request):
    data = {}
    if request.method == 'POST':
        datos = json.loads(request.POST['datos'])
        for sub in datos:
            p = str(sub['periodo'])
            m = str(sub['materia'])
            c = str(sub['curso'])
            d = int(sub['docente'])
            if p == "" or m == "" or c == "":
                data['error'] = "Existe un campo vacio por favor completalo y vuelve a intentarlo"
                data['resp'] = False
            else:
                if Asignar.objects.filter(materia_id=m, curso_id=c, periodo_id=p, docente_id=d):
                    data['error'] = "Ya existe un registro igual por favor verificalo y vuelve a intentarlo"
                    data['resp'] = False
                else:
                    if Asignar.objects.filter(materia_id=m, curso_id=c, periodo_id=p):
                        data[
                            'error'] = "Materia y curso ya Asignados a un Docente <br> por favor verificalo y vuelve a intentarlo"
                        data['resp'] = False
                    else:
                        n = Asignar()
                        n.docente_id = d
                        n.materia_id = m
                        n.curso_id = c
                        n.periodo_id = p
                        n.save()
                        data['resp'] = True
        return HttpResponse(json.dumps(data), content_type="application/json")


def Lista_Asignadas(request):
    Asignadas = Asignar.objects.all()
    contexto = {'Asignadas': Asignadas}
    return render(request, "back-end/asignar/asignar_list.html", contexto)


def Lista_Asignadas_docente(request):
    Asignadas = Asignar.objects.filter(docente_id=request.user.id).distinct("materia_id")
    contexto = {'Asignadas': Asignadas}
    return render(request, "back-end/asignar/asignar_list_docente.html", contexto)


def Lista_cursos(request, id_curso, id_periodo):
    Asignadas = Asignar.objects.filter(docente_id=request.user.id, curso_id=id_curso, periodo_id=id_periodo).distinct(
        "materia_id")
    contexto = {'Asignadas': Asignadas}
    return render(request, "back-end/asignar/asignar_list_docente_curso.html", contexto)


def Lista_Asignadas_admin(request, id_docente):
    Asignadas = Asignar.objects.filter(docente_id=id_docente).distinct("materia_id")
    contexto = {'Asignadas': Asignadas, "id_docente": id_docente}
    return render(request, "back-end/asignar/asignar_list_docente.html", contexto)


def editar(request, id_asignar):
    asignar = Asignar.objects.get(id=id_asignar)
    opc_edit = '/asignar/editar/' + id_asignar + '/'
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_edit, 'entidad': opc_entidad,
        'boton': 'Guardar Asignacion', 'titulo': 'Editar Registro de una Asignacion',
    }

    if request.method == 'GET':
        form = AsignarForm(instance=asignar)
        data['form'] = form
    else:
        form = AsignarForm(request.POST, instance=asignar)
        if Asignar.objects.filter(materia_id=form.data['materia'], curso_id=form.data['curso'],
                                  periodo_id=form.data['periodo'],
                                  docente_id=form.data['docente']):
            if form.is_valid():
                form.save()
            return redirect('asignar:listado')
        else:
            if Asignar.objects.filter(materia_id=form.data['materia'], curso_id=form.data['curso'],
                                      periodo_id=form.data['periodo']).exclude(docente_id=form.data['docente']):
                data['errorrep'] = "Materia y Curso ya asignados a un Docente en el mismo periodo " \
                                   "por favor verificalo y vuelve a intentarlo"
                data['form'] = form
                return render(request, 'back-end/asignar/asignar_form2.html', data)
            else:
                if form.is_valid():
                    form.save()
                return redirect('asignar:listado')
    return render(request, 'back-end/asignar/asignar_form2.html', data)
