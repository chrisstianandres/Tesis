from django.shortcuts import render, redirect
from .forms import *
import json
from .models import Silabo
from django.http import *

opc_icono = 'fa fa-archive'
opc_ruta = '/silabo/nuevo'
opc_nuevo = '/silabo/nuevo'
opc_crud = '/silabo/crear'
opc_delete = '/silabo/borrar'
opc_entidad = 'Planes de Clase'


def nuevo(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Plan de Clase', 'action': 'add', 'titulo': 'Nuevo Registro de un Plan de Clase',
    }
    if request.method == 'GET':
        data['form'] = SilaboForm()
    return render(request, 'back-end/silabo/silabo_form.html', data)

def silabo_list(request):
    data = {
        'icono': opc_icono, 'ruta': '/silabo/listado', 'crud': opc_crud, 'entidad': opc_entidad,
        'titulo': 'Planes de Clase Generales',
    }
    if request.method == 'GET':
        data['form'] = SilaboForm()
    return render(request, 'back-end/silabo/silabo_general.html', data)

def editar(request, id):

    silabo = Silabo.objects.get(id=id)
    opc_edit = '/silabo/editar/'+id+'/'
    a = Silabo.objects.get(id=id)
    b = str(a.materia.id)
    m = str(a.materia.nombre)
    back ='/materia/plan/'+b+'/'

    if request.method == 'GET':
        form = SilaboFormEdit(instance=silabo)
    else:
        form = SilaboFormEdit(request.POST, instance=silabo)
        if form.is_valid():
            form.save()
        return redirect(back)
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_edit, 'entidad': opc_entidad,
        'boton': 'Guardar Plan de clase',  'titulo': 'Editar Registro de'+' ' + m +'',
        'form': form
    }

    return render(request, 'back-end/asignar/asignar_form2.html', data)



def get_silabo(request):
    materia_id = request.GET.get('materia_id')
    if materia_id:
        data = [[silabo.id, silabo.semana, silabo.unidad, silabo.clase, silabo.tema, silabo.id, silabo.id]
                for silabo in Silabo.objects.filter(materia_id=materia_id)]
        return HttpResponse(json.dumps(data), content_type="application/json")

def get_last_silabo(request):
    materia_id = request.GET.get('materia_id')
    int(materia_id)
    if materia_id:
        data = [[silabo.semana, silabo.unidad, silabo.clase, silabo.tema]
                for silabo in Silabo.objects.raw('SELECT *  FROM silabo where materia_id=%s ORDER BY id DESC LIMIT 1;',
                                                 [materia_id])]
        return HttpResponse(json.dumps(data), content_type="application/json")

def save_silabo(request):
    data = {}
    if request.method == 'POST':
        datos = json.loads(request.POST['datos'])
        for sub in datos:
            s = sub['semana']
            str(s)
            u = sub['unidad']
            str(u)
            c = sub['clase']
            str(c)
            t = sub['tema']
            str(t)
            m = sub['materia']
            if s == "" or u == "" or c == "" or t == "":
                data['error'] = "Existe un campo vacio por favor completalo y vuelve a intentarlo"
                data['resp'] = False
            else:
                s = sub['semana']
                int(s)
                u = sub['unidad']
                int(u)
                c = sub['clase']
                int(c)
                m = sub['materia']
                int(m)
                if Silabo.objects.filter(materia=m):
                    if Silabo.objects.filter(materia=m, semana=s):
                        if Silabo.objects.filter(materia=m, semana=s, unidad=u):
                            print("misma unidad")
                            if Silabo.objects.filter(materia=m, semana=s, unidad=u, clase=c):
                                print("misma clase")
                                if Silabo.objects.filter(materia=m, semana=s, unidad=u, clase=c, tema=t):
                                    print("misma tema")
                                    data['error'] = "Ya existe un tema igual registrado"
                                    data['resp'] = False
                                else:
                                    n = Silabo()
                                    n.materia_id = m
                                    n.semana = s
                                    n.unidad = u
                                    n.clase = c
                                    n.tema = t
                                    n.save()
                                    data['resp'] = True
                            else:
                                n = Silabo()
                                n.materia_id = m
                                n.semana = s
                                n.unidad = u
                                n.clase = c
                                n.tema = t
                                n.save()
                                data['resp'] = True
                        else:
                            n = Silabo()
                            n.materia_id = m
                            n.semana = s
                            n.unidad = u
                            n.clase = c
                            n.tema = t
                            n.save()
                            data['resp'] = True
                    else:
                        n = Silabo()
                        n.materia_id = m
                        n.semana = s
                        n.unidad = u
                        n.clase = c
                        n.tema = t
                        n.save()
                        data['resp'] = True
                else:
                    n = Silabo()
                    n.materia_id = m
                    n.semana = s
                    n.unidad = u
                    n.clase = c
                    n.tema = t
                    n.save()
                    data['resp'] = True
        return HttpResponse(json.dumps(data), content_type="application/json")

def eliminar(request):
    data = {}
    if request.method == 'POST':
        try:
            h = Silabo.objects.get(pk=request.POST['id'])
            h.delete()
            data['resp'] = True
        except Exception as e:
            data['error'] = e.message
            data['resp'] = False
    return HttpResponse(json.dumps(data), content_type="application/json")



