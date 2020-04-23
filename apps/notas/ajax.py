from django.http import JsonResponse, HttpResponse
import json
from django.db.models import Count
from .models import Asignar, Listado
from apps.quimestre.models import *
from apps.parcial.models import *
from ..notas.models import Notas
from ..asistencias.models import *


def get_periodo(request):
    a = request.user.id
    periodos = Asignar.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if a:
        periodos = Asignar.objects.filter(docente_id=a).distinct("periodo_id")
    for periodo in periodos:
        options += '<option value="%s">%s</option>' % (
            periodo.periodo_id,
            periodo.periodo
        )
    response = {}
    response['periodos'] = options
    return JsonResponse(response)

def get_materia(request):
    a = request.user.id
    periodo_id = request.GET.get('periodo_id')
    materias = Asignar.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if periodo_id:
        materias = Asignar.objects.filter(periodo_id=periodo_id, docente_id=a).distinct("materia_id")
    for materia in materias:
        options += '<option value="%s">%s</option>' % (
            materia.materia.id,
            materia.materia.nombre
        )
    response = {}
    response['materias'] = options
    return JsonResponse(response)

def get_curso(request):
    a = request.user.id
    materia_id = request.GET.get('materia_id')
    periodo_id = request.GET.get('periodo_id')
    docente_id = request.user.id
    cursos = Asignar.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if materia_id:
        cursos = Asignar.objects.filter(periodo_id=periodo_id, docente_id=docente_id, materia_id=materia_id).distinct("curso_id")
    for curso in cursos:
        options += '<option value="%s">%s</option>' % (
            curso.curso.pk,
            curso.curso
        )
    response={}
    response['cursos'] = options
    response['asignar'] = options
    return JsonResponse(response)

def get_curso_asistencias(request):
    materia_id = request.GET.get('materia_id')
    periodo_id = request.GET.get('periodo_id')
    docente_id = request.user.id
    cursos = Asignar.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if materia_id:
        cursos = Asignar.objects.filter(periodo_id=periodo_id, docente_id=docente_id, materia_id=materia_id).distinct("curso_id")
    for curso in cursos:
        options += '<option value="%s">%s</option>' % (
            curso.pk,
            curso.curso
        )
    response={}
    response['cursos'] = options
    response['asignar'] = options
    return JsonResponse(response)

def get_parcial(request):
    quimestre_id = request.GET.get('quimestre_id')
    parciales = Parcial.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if quimestre_id:
        parciales = Parcial.objects.filter(quimestre=quimestre_id)
    for p in parciales:
        options += '<option value="%s"> Parcial %s</option>' % (
            p.pk,
            p.numero
        )
    response={}
    response['parciales'] = options
    return JsonResponse(response)

def get_alumno(request):
    a = request.user.id
    periodo_id = request.GET.get('periodo_id')
    curso_id = request.GET.get('curso_id')
    materia_id = request.GET.get('materia_id')
    asignar= Asignar.objects.get(docente=a, curso_id=curso_id, materia_id=materia_id, periodo_id=periodo_id)

    if periodo_id and curso_id:
     data = [[a.alumno.apellidos +" "+a.alumno.nombres, a.id, a.id, asignar.id]
                 for a in Listado.objects.filter(periodo_id=periodo_id, curso_id=curso_id,
                                                 curso__asignar__docente_id=a, alumno__estado=0).order_by('-alumno_id').distinct('alumno_id')]

     return HttpResponse(json.dumps(data), content_type="application/json")

def get_alumno_asistencias(request):
    a = request.user.id
    periodo_id = request.GET.get('periodo_id')
    curso_id = request.GET.get('curso_id')
    materia_id = request.GET.get('materia_id')
    desde = request.GET.get('desde')
    hasta = request.GET.get('hasta')
    if periodo_id and curso_id and materia_id and desde and hasta:
     data = [[a.Listado.alumno.apellidos +" "+a.Listado.alumno.nombres, a.get_Asistencia_display(), a.fecha.strftime("%d/%m/%Y")]
             for a in Asistencias.objects.filter(Listado__periodo_id=periodo_id, Horario__asignar__curso_id=curso_id,
                                                 Horario__asignar__materia_id=materia_id,
                                                 Horario__asignar__docente_id=a, fecha__range=[desde, hasta])]
     return HttpResponse(json.dumps(data), content_type="application/json")

def save_note(request):
    data = {}
    if request.method == 'POST':
        datos = json.loads(request.POST['datos'])
        n=Notas()
        for sub in datos:
            if Notas.objects.filter(Asignar=sub['asignar'], Listado=sub['lista']):
                g = Notas.objects.get(Listado_id=sub['lista'])
                if g.Parcial_1_q_1 > 0:
                    if sub['parcial'] == "2":
                        if g.Parcial_2_q_1 == 0:
                            g.Parcial_2_q_1 = sub['nota']
                            g.save()
                            data['resp'] = True
                        else:
                            data['error'] = "Ya existe notas registradas para el Parcial 2 del Primer Quimestre"
                            data['resp'] = False
                    elif sub['parcial'] == "3":
                        if g.Parcial_3_q_1 == 0:
                            g.Parcial_3_q_1 = sub['nota']
                            g.save()
                            data['resp'] = True
                        else:
                            data['error'] = "Ya existe notas registradas para el Parcial 3 del Primer Quimestre"
                            data['resp'] = False
                    elif sub['parcial'] == "4":
                        if g.Parcial_1_q_2 == 0:
                            g.Parcial_1_q_2 = sub['nota']
                            g.save()
                            data['resp'] = True
                        else:
                            data['error'] = "Ya existe notas registradas para el Parcial 1 del Segundo Quimestre"
                            data['resp'] = False
                    elif sub['parcial'] == "5":
                        if g.Parcial_2_q_2 == 0:
                            g.Parcial_2_q_2 = sub['nota']
                            g.save()
                            data['resp'] = True
                        else:
                            data['error'] = "Ya existe notas registradas para el Parcial 2 del Segundo Quimestre"
                            data['resp'] = False
                    elif sub['parcial'] == "6":
                        if g.Parcial_3_q_2 == 0:
                            g.Parcial_3_q_2 = sub['nota']
                            g.save()
                            data['resp'] = True
                            if g.Nota_final >= 7:
                                lis = Listado.objects.get(id=sub['lista'])
                                lis.estado = 3
                                lis.save()
                        else:
                            data['error'] = "Ya existe notas registradas para el Parcial 3 del Segundo Quimestre"
                            data['resp'] = False
                    elif sub['parcial'] == "10":
                        if g.examen_final == 0:
                            g.examen_final = sub['nota']
                            g.save()
                            data['resp'] = True
                            lis = Listado.objects.get(id=sub['lista'])
                            lis.estado = 3
                            lis.save()
                        else:
                            data['error'] = "Ya existe nota de Examen Final Registrada"
                            data['resp'] = False
                    else:
                        data['error'] = "Ya existe notas registradas para el Parcial 1 del Primer Quimestre"
                        data['resp'] = False
            elif sub['parcial'] == "1":
                n = Notas()
                a = sub['asignar']
                b = sub['lista']
                n.Asignar_id = a
                n.Listado_id = b
                n.Parcial_1_q_1 = sub['nota']
                n.save()
                data['resp'] = True
            elif sub['parcial'] == 10 and n.Parcial_1_q_1 == 0 and n.Parcial_2_q_1 == 0 and n.Parcial_3_q_1 == 0\
                    or n.Parcial_1_q_2 == 0 or n.Parcial_2_q_2 == 0 or n.Parcial_3_q_2:
                    data['error'] = "<H4><strong>Nota de examen no admitida </strong></H4><br> No puede ingresar una nota de examen final sin " \
                                    "antes haber ingresado las notas parciales <br>" \
                                    "<H5><strong>POR FAVOR VERIFICALO Y VUELVE A INTENTARLO</strong></H5>"
                    data['resp'] = False
            else:
                data[
                    'error'] = "<H4><strong>Nota de examen no admitida </strong></H4><br> No puede ingresar una nota de examen final sin " \
                               "antes haber ingresado las notas parciales <br>" \
                               "<H5><strong>POR FAVOR VERIFICALO Y VUELVE A INTENTARLO</strong></H5>"
                data['resp'] = False

    return HttpResponse(json.dumps(data), content_type="application/json")

def get_fecha (request):
    consulta1 = Asistencias.objects.order_by('-fecha').first()
    consulta2 = Asistencias.objects.order_by('-fecha').last()
    hasta = consulta1.fecha.strftime("%Y/%m/%d")
    desde = consulta2.fecha.strftime("%Y/%m/%d")
    response = {}
    response['hasta'] = hasta
    response['desde'] = desde
    return HttpResponse(json.dumps(response), content_type="application/json")

def get_notas(request):
    a = request.user.id
    periodo_id = request.POST['periodo_id']
    curso_id = request.POST['curso_id']
    materia_id = request.POST['materia_id']
    if periodo_id and curso_id and materia_id:
        data = [[a.Listado.alumno.apellidos + " " + a.Listado.alumno.nombres, a.Parcial_1_q_1, a.Parcial_2_q_1,
                 a.Parcial_3_q_1, a.Parcial_1_q_2, a.Parcial_2_q_2, a.Parcial_3_q_1, a.Quimestre_1, a.Quimestre_2,
                 a.examen_final, a.Nota_final]
                for a in Notas.objects.filter(Listado__periodo_id=periodo_id, Listado__curso_id=curso_id,
                                              Asignar__materia_id=materia_id, Asignar__curso_id=curso_id,
                                              Asignar__docente_id=a)]

        return HttpResponse(json.dumps(data), content_type="application/json")