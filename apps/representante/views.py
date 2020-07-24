from django.shortcuts import render, redirect
from .models import *
from apps.representante.models import *
from django.urls import reverse_lazy
from django.views.generic import *
import json
from django.http import HttpResponse
from apps.representante.forms import RepresentanteForm
from django.http import HttpResponseRedirect
from apps.alumno.models import *
from apps.representante.models import *
from apps.docente.models import *

opc_icono = 'fa fa-group'
opc_ruta = '/representante/'
opc_nuevo = '/representante/nuevo'
opc_crud = '/representante/crear/'
opc_delete = '/representante/borrar'
opc_entidad = 'Representantes'


def nuevo(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Representante', 'action': 'add', 'titulo': 'Nuevo Registro de un Representante',
    }
    if request.method == 'GET':
        data['form'] = RepresentanteForm()
    return render(request, 'back-end/representante/representante_form.html', data)


def crear(request):
    f = RepresentanteForm(request.POST)
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Representante', 'action': 'add', 'titulo': 'Nuevo Registro de un Representante',
    }
    action = request.POST['action']
    data['action'] = action
    if request.method == 'POST' and 'action' in request.POST:
        if action == 'add':
            f = RepresentanteForm(request.POST)
            if f.is_valid():
                f.save(commit=False)
                if Alumno.objects.filter(cedula=f.data['cedula']):
                    data['errorrep'] = 'Numero de Cedula ya exitente en los respresentantes'
                    data['form'] = f
                    return render(request, 'back-end/representante/representante_form.html', data)
                else:
                    if Docente.objects.filter(cedula=f.data['cedula']):
                        data['errorrep'] = 'Numero de Cedula ya exitente en los Docentes'
                        data['form'] = f
                        return render(request, 'back-end/representante/representante_form.html', data)
                    else:
                        a = verificar(f.data['cedula'])
                        if a == False:
                            data['errorrep'] = 'Numero de Cedula no coressponde a digitos para Ecuador'

                            data['form'] = f
                            return render(request, 'back-end/representante/representante_form.html', data)
                        else:
                            f.save()
                            return HttpResponseRedirect('/alumnos/nuevo')
            else:
                data['form'] = f
                return render(request, 'back-end/representante/representante_form.html', data)

def listado(request):
    lista = Representante.objects.all()
    contexto = {"lista": lista, 'titulo': 'Listado de Representantes'}
    return render(request, 'back-end/representante/representante_list.html', contexto)

def editar(request, id_representante):
    representante = Representante.objects.get(id=id_representante)
    opc_edit = '/representante/editar/' + id_representante + '/'
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_edit, 'entidad': opc_entidad,
        'boton': 'Guardar Representante', 'titulo': 'Editar Registro de un Representante',
    }
    if request.method == 'GET':
        f = RepresentanteForm(instance=representante)
    else:
        f = RepresentanteForm(request.POST, instance=representante)
        if f.is_valid():
            f.save(commit=False)
            if Alumno.objects.filter(cedula=f.data['cedula']):
                data['errorrep'] = 'Numero de Cedula ya exitente en los respresentantes'
                data['form'] = f
                return render(request, 'back-end/representante/representante_form.html', data)
            else:
                if Docente.objects.filter(cedula=f.data['cedula']):
                    data['errorrep'] = 'Numero de Cedula ya exitente en los Docentes'
                    data['form'] = f
                    return render(request, 'back-end/representante/representante_form.html', data)
                else:
                    a = verificar(f.data['cedula'])
                    if a == False:
                        data['errorrep'] = 'Numero de Cedula no coressponde a digitos para Ecuador'

                        data['form'] = f
                        return render(request, 'back-end/representante/representante_form.html', data)
                    else:
                        f.save()
                        return HttpResponseRedirect('/alumnos/nuevo')
        else:
            data['form'] = f
            return render(request, 'back-end/representante/representante_form.html', data)
    data['form'] = f
    return render(request, 'back-end/representante/representante_form.html', data)

def verificar(nro):
    l = len(nro)
    if l == 10 or l == 13: # verificar la longitud correcta
        cp = int(nro[0:2])
        if cp >= 1 and cp <= 22: # verificar codigo de provincia
            tercer_dig = int(nro[2])
            if tercer_dig >= 0 and tercer_dig < 6 : # numeros enter 0 y 6
                if l == 10:
                    return __validar_ced_ruc(nro,0)
                elif l == 13:
                    return __validar_ced_ruc(nro,0) and nro[10:13] != '000' # se verifica q los ultimos numeros no sean 000
            elif tercer_dig == 6:
                return __validar_ced_ruc(nro,1) # sociedades publicas
            elif tercer_dig == 9: # si es ruc
                return __validar_ced_ruc(nro,2) # sociedades privadas
            else:
                raise Exception(u'Tercer digito invalido')
        else:
            raise Exception(u'Codigo de provincia incorrecto')
    else:
        raise Exception(u'Longitud incorrecta del numero ingresado')

def __validar_ced_ruc(nro,tipo):
    total = 0
    if tipo == 0: # cedula y r.u.c persona natural
        base = 10
        d_ver = int(nro[9])# digito verificador
        multip = (2, 1, 2, 1, 2, 1, 2, 1, 2)
    elif tipo == 1: # r.u.c. publicos
        base = 11
        d_ver = int(nro[8])
        multip = (3, 2, 7, 6, 5, 4, 3, 2 )
    elif tipo == 2: # r.u.c. juridicos y extranjeros sin cedula
        base = 11
        d_ver = int(nro[9])
        multip = (4, 3, 2, 7, 6, 5, 4, 3, 2)
    for i in range(0,len(multip)):
        p = int(nro[i]) * multip[i]
        if tipo == 0:
            total+=p if p < 10 else int(str(p)[0])+int(str(p)[1])
        else:
            total+=p
    mod = total % base
    val = base - mod if mod != 0 else 0
    return val == d_ver

