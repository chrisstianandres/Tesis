from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import *
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .models import *
from apps.horario.models import *
from apps.asistencias.forms import *
from apps.asistencias.models import Asistencias
import json


def alumno_list(request):
    a = request.user.id
    materia = request.GET.get('materia')
    nomCurso = request.GET.get('nomCurso')
    listaalumno = Asistencias.objects.raw('SELECT max(horario."id") AS id,curso.nombre , '
                                          'lista_listado."id" as idlista, alumno.nombres,'
                                          'alumno.apellidos,current_date as hoy, materia.nombre as materia  '
                                          'FROM horario INNER JOIN curso ON horario.curso_id = curso."id" '
                                          'INNER JOIN lista_listado ON lista_listado.curso_id = curso."id" '
                                          'INNER JOIN alumno ON lista_listado.alumno_id = alumno."id" '
                                          'INNER JOIN silabo ON "public".horario.silabo_id= silabo."id" '
                                          'INNER JOIN materia ON silabo.materia_id = materia."id"  '
                                          'WHERE horario.docente_id= %s and curso.nombre= %s  '
                                          'and materia.nombre = %s GROUP BY curso.nombre , lista_listado."id",'
                                          'alumno.nombres,alumno.apellidos,materia.nombre '
                                          'order by alumno.apellidos asc ', [a, nomCurso, materia])
    contexto = {'listaalumno': listaalumno}

    return render(request, "back-end/alumno/alumnoindex.html", contexto)
def alumno_list2(request):
    p= 'Presente'
    f='Falta'
    a = request.user.id
    materia = request.GET.get('materia')
    fecha = request.GET.get('fecha')
    nomCurso = request.GET.get('nomCurso')
    listaalumno = Asistencias.objects.raw('SELECT alumno.nombres, alumno.apellidos, '
                                          'asistencias_asistencias."Asistencia" '
                                          'AS "id",Case asistencias_asistencias."Asistencia"  WHEN 1 THEN %s WHEN 0 '
                                          'THEN %s END as Asistencia, asistencias_asistencias.fecha, '
                                          'curso.nombre AS curso, materia.nombre AS materia, horario.docente_id '
                                          'FROM asistencias_asistencias '
                                          'INNER JOIN lista_listado ON '
                                          '"public".asistencias_asistencias."Listado_id" = "public".lista_listado."id" '
                                          'INNER JOIN alumno ON lista_listado.alumno_id = alumno."id" '
                                          'INNER JOIN curso ON lista_listado.curso_id = curso."id" '
                                          'INNER JOIN horario ON horario.curso_id = curso."id" '
                                          'AND asistencias_asistencias."Horario_id" = horario."id" '
                                          'INNER JOIN silabo ON horario.silabo_id = silabo."id" '
                                          'INNER JOIN materia ON silabo.materia_id = materia."id" '
                                          'WHERE materia.nombre=%s AND curso.nombre = %s '
                                          'AND asistencias_asistencias.fecha = %s AND horario.docente_id = %s '
                                          'GROUP BY alumno.nombres, alumno.apellidos, '
                                          'asistencias_asistencias."Asistencia", '
                                          'asistencias_asistencias.fecha,curso.nombre , '
                                          'materia.nombre, horario.docente_id '
                                          'order by alumno.apellidos asc', [p, f, materia, nomCurso, fecha, a])
    contexto = {'listaalumno': listaalumno}

    return render(request, "back-end/alumno/alumnoindex2.html", contexto)
def asistencia_list_fecha(request):
    a = request.user.id
    materia = request.GET.get('materia')
    nomCurso = request.GET.get('nomCurso')
    listaasistencia = Asistencias.objects.raw('SELECT asistencias_asistencias.fecha as id, curso.nombre, '
                                              'materia.nombre as materia,horario.docente_id  '
                                              'FROM asistencias_asistencias '
                                              'INNER JOIN lista_listado '
                                              'ON asistencias_asistencias."Listado_id" = lista_listado."id" '
                                              'INNER JOIN curso ON lista_listado.curso_id = curso."id" '
                                              'INNER JOIN horario ON horario.curso_id = curso."id" '
                                              'AND asistencias_asistencias."Horario_id" = horario."id" '
                                              'INNER JOIN silabo ON horario.silabo_id = silabo."id" '
                                              'INNER JOIN materia ON silabo.materia_id = materia."id" '
                                              'WHERE materia.nombre = %s and curso.nombre= %s and '
                                              'horario.docente_id =%s GROUP BY horario.docente_id,'
                                              'asistencias_asistencias.fecha, "public".curso.nombre, '
                                              'materia.nombre', [materia, nomCurso, a])
    contexto = {'listaasistencia': listaasistencia}
    return render(request, "back-end/asistencia/asistenciaindex_fechas.html", contexto)
def vista_asistencias(request):
    form = AsistenciasForm()
    if request.method == 'POST':
        form = AsistenciasForm(request.POST)
    return render(request, 'back-end/asistencia/asistencias_form.html', {'form': form})

def get_asistencias(request):
    materiaId = request.POST["materia_id"]
    periodoId = request.POST["periodo_id"]
    cursoId = request.POST["curso_id"]
    desde = request.POST["desde"]
    hasta = request.POST["hasta"]
    data = transpose(materiaId, periodoId, cursoId, desde, hasta)
    if data:
        df = pd.DataFrame(data)
        df.fillna('0', inplace=True)
        pivot = pd.pivot_table(df, index=['Alumno'], values=['Asistencia'], columns=['Fecha'], aggfunc='mean')
        html2 = pivot.to_html(table_id='asistencia', classes='table table-striped table-bordered table-hover')
        response = {"tablaHtml": html2}
    else:
        response = {"resp": 'False'}
    return HttpResponse(json.dumps(response), content_type="application/json")



def transpose(materiaId, periodoId, cursoId, desde, hasta):
    asistencias = Asistencias.objects.filter(Horario__asignar__materia_id=materiaId, Listado__curso_id=cursoId,
                                             Listado__periodo_id=periodoId, fecha__range=[desde, hasta])
    data = [{'Alumno': a.Listado.alumno.apellidos+' '+a.Listado.alumno.nombres, 'Fecha': a.fecha,
             'Asistencia': a.Asistencia} for a in asistencias]
    return data


@csrf_exempt
def save_asistencia(request):
    data = {}
    fecha_hoy = date.today()
    if request.method == 'POST':
        datos = json.loads(request.POST['datos'])
        for sub in datos:
           if Asistencias.objects.filter(Horario_id=sub['horario'], Listado_id=sub['listado'], fecha=fecha_hoy):
               data['resp'] = False
               data['error'] = 'Ya existe un registro de esta hora'
           else:
               h = Horario.objects.get(pk=sub['horario'])
               h.asist_alum = 2
               h.save()
               n = Asistencias()
               n.Horario_id = sub['horario']
               n.Listado_id = sub['listado']
               n.fecha = fecha_hoy
               n.Asistencia = sub['asistencia']
               n.save()
               data['resp'] = True
        return HttpResponse(json.dumps(data), content_type="application/json")