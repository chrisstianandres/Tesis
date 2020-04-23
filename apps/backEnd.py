# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import *
from django.http import HttpResponse
from django.http import *
from .horario.models import *
from .registro.models import *
import json
from .notas.models import *
from .asistencias.models import Asistencias
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

#-----------------------------------------------PAGINA PRINCIPAL-----------------------------------------------------#
def menu(request):
    data = {
        'titulo': 'Menu Principal'
    }
    return render(request, 'back-end/menu_principal.html', data)

def horario_json(request):
    fecha_hoy = date.today()
    data = [[h.id, h.hora_inicio, h.hora_fin, h.asignar.curso.nombre, h.asignar.curso.aula.numero, h.silabo.materia.nombre, h.silabo.tema,
         h.silabo.unidad, h.silabo.semana, h.asist_alum, h.estado] for h in Horario.objects.filter(asignar__docente__id=request.user.id, fecha=fecha_hoy)]
    return HttpResponse(json.dumps(data), content_type="application/json")

def horario_json_admin(request):
    fecha_hoy = date.today()
    data = [[h.id, str(h.asignar.docente), h.hora_inicio, h.hora_fin, h.asignar.curso.nombre, h.asignar.curso.aula.numero, h.silabo.materia.nombre, h.silabo.tema,
         h.silabo.unidad, h.silabo.semana, h.asist_alum, h.estado] for h in Horario.objects.filter(fecha=fecha_hoy)]
    return HttpResponse(json.dumps(data), content_type="application/json")

def actividad_id(request):
    data = [[a.id, a.alumno.__str__(), a.nombre, a.id] for a in Actividad.objects.filter(horario_id=request.POST['id'])]
    return HttpResponse(json.dumps(data), content_type="application/json")

def registrar_clase(request):
    data = {}
    if request.method == 'POST':
        try:
            r = Registro()
            r.horario_id = request.POST['id']
            r.save()
            h = Horario.objects.get(pk=request.POST['id'])
            h.estado = 2
            h.save()
            data['resp'] = True
        except Exception as e:
            data['error'] = e.message
            data['resp'] = False
    return HttpResponse(json.dumps(data), content_type="application/json")

#-----------------------------------------------Asistencia----------------------------------------------------------------#
def asistencia_registrar(request):
        #json.loads para convertir el string en json
        datos = json.loads(request.POST['datos'])
        fecha_hoy = date.today()
        for sub in datos:
            a = Asistencias()
            a.Horario_id = sub['horario']
            a.Listado_id = sub['lista']
            a.Asistencia = sub['asistencia']
            a.fecha = fecha_hoy
            a.save()
        return HttpResponse(json.dumps(datos), content_type="application/json")

#-----------------------------------------------LOGEO----------------------------------------------------------------#
def logeo(request):
    data = {
        'titulo': 'Inicio de sesión'
    }
    return render(request, 'back-end/registration/login2.html', data)

def connect(request):
    data = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if (user.docente.estado == 1 or user.docente.estado == 2):
                data['error'] = 'Usuario Inavilitado.'
            else:
                login(request, user)
                data['resp'] = True
        else:
            data['error'] = 'Usuario no valido.'
    else:
        data['error'] = 'Metodo Request no es Valido.'
    return HttpResponse(json.dumps(data), content_type="application/json")

def disconnect(request):
    logout(request)
    return HttpResponseRedirect('/login')

#-----------------------------------------------NOTAS----------------------------------------------------------------#
def notas(request):
    return render(request, 'back-end/notas/notas_form_report_net.html')

def notas_net(request):
    data = {}
    cedula= request.POST['cedula']
    if cedula:
        alumno = Alumno.objects.filter(cedula=cedula)
        if alumno:
           for a in alumno:
            data2 = {
                "nombre": a.nombres+' '+a.apellidos,
                "fecha": a.fecha_nacimiento.strftime("%d/%m/%Y"),
                "representante": a.representante.__str__(),
                "correo": a.correo,
                "sexo": a.get_sexo_display()
            }
            data['data'] = data2
            periodos = Listado.objects.filter(alumno__cedula=cedula).order_by("periodo_id").distinct("periodo_id")
            options = '<option value="" selected="selected">---------</option>'
            for periodo in periodos:
                options += '<option value="%s">%s</option>' % (
                    periodo.periodo.pk,
                    periodo.periodo,
                )
            data['periodos'] = options
            data['resp'] = True
        else:
            data['error'] = "N\u00FAmero de c\u00E9dula incompleto o no v\u00E1lido"
            data['resp'] = False
    else:
        data['error'] = "N\u00FAmero de c\u00E9dula incompleto o no v\u00E1lido"
        data['resp'] = False
    return HttpResponse(json.dumps(data), content_type="application/json")

def notas_alumnos(request):
    cedula = request.POST["cedula"]
    periodo = request.POST["periodo"]
    data = [[h.Asignar.materia.nombre, h.Parcial_1_q_1, h.Parcial_2_q_1, h.Parcial_3_q_1,
             h.Parcial_1_q_2, h.Parcial_2_q_2, h.Parcial_3_q_2,
         h.Quimestre_1, h.Quimestre_2, h.examen_final, h.Nota_final]
            for h in Notas.objects.filter(Listado__alumno__cedula=cedula, Asignar__periodo_id=periodo)]

    return HttpResponse(json.dumps(data), content_type="application/json")