from django.shortcuts import render, redirect
from apps.docente.models import Docente
from apps.asignar.models import Asignar
from apps.docente.forms import DocenteForm
from django.http import *
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from django.views.generic import View
from reportlab.lib import colors
from reportlab.platypus import TableStyle, Table
from datetime import date
import json
from django.db.models import Q

# ---------------------------
opc_icono = 'fa fa-user-o'
opc_ruta = '/docente/'
opc_nuevo = '/docente/nuevo/'
opc_crud = '/docente/crear/'
opc_delete = '/docente/borrar'
opc_entidad = 'Docentes'


# ---------------------------
def nuevo(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Docente', 'action': 'add', 'titulo': 'Nuevo Registro de un Docente',
    }
    if request.method == 'GET':
        data['form'] = DocenteForm()
        return render(request, 'back-end/docente/docenteForm.html', data)


def crear(request):
    f = DocenteForm(request.POST)
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud
    }
    action = request.POST['action']
    data['action'] = action
    if request.method == 'POST' and 'action' in request.POST:
        if action == 'add' or action == 'edit':
            if action == 'add':
                f = DocenteForm(request.POST or None, request.FILES or None)
            elif action == 'edit':
                f = DocenteForm(request.POST, instance=Docente.objects.get(id=request.POST['id']))
            if f.is_valid():
                f.save()
            else:
                data = {
                    'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
                    'boton': 'Guardar Docente', 'action': 'add', 'titulo': 'Nuevo Registro de un Docente',
                    'form': f
                }
                return render(request, 'back-end/docente/docenteForm.html', data)
            return HttpResponseRedirect('/docente/listado')


def Docente_list(request):
    Docente_list = Docente.objects.all()
    contexto = {'Docente_list': Docente_list}
    return render(request, "back-end/docente/Docente_list.html", contexto)


def editar(request, id_docente):
    docente = Docente.objects.get(id=id_docente)
    opc_edit = '/docente/editar/' + id_docente + '/'

    if request.method == 'GET':
        form = DocenteForm(instance=docente)
    else:
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
        return redirect('docente:Docente_list')
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_edit, 'entidad': opc_entidad,
        'boton': 'Guardar Docente', 'titulo': 'Editar Registro de un Docente',
        'form': form
    }

    return render(request, 'back-end/docente/docenteForm.html', data)

def eliminar(request):
    data = {}
    if request.method == 'POST':
        try:
            h = Docente.objects.get(pk=request.POST['id'])
            h.delete()
            data['resp'] = True
        except Exception as e:
            data['error'] = e.message
            data['resp'] = False
    return HttpResponse(json.dumps(data), content_type="application/json")




def estado(request):
    data = {}
    if request.method == 'POST':
        try:
            fecha_hoy = date.today()
            ano = fecha_hoy.year + 1
            h = Docente.objects.get(pk=request.POST['id'])
            h.estado = request.POST['estado']
            h.save()
            r = int(request.POST['estado'])
            if r == 0:
                m = Asignar.objects.filter(
                    Q(periodo__periodo_fin__year=fecha_hoy.year) | Q(periodo__periodo_fin__year=ano),
                    Q(estado=1) | Q(estado=2), docente_id=request.POST['id'])
                for n in m:
                    n.estado = 0
                    n.save()
            if r == 1:
                m = Asignar.objects.filter(
                    Q(periodo__periodo_fin__year=fecha_hoy.year) | Q(periodo__periodo_fin__year=ano),
                    docente_id=request.POST['id'], estado=0)
                for n in m:
                    n.estado = 1
                    n.save()
            if r == 2:
                m = Asignar.objects.filter(
                    Q(periodo__periodo_fin__year=fecha_hoy.year) | Q(periodo__periodo_fin__year=ano),
                    docente_id=request.POST['id'], estado=0)
                for n in m:
                    n.estado = 2
                    n.save()
            data['resp'] = True
        except Exception as e:
            data['error'] = e.message
            data['resp'] = False
    return HttpResponse(json.dumps(data), content_type="application/json")


def profile(request):

    return render(request, 'back-end/docente/profile.html')

class ReportePersonasPDF(View):

    def cabecera(self, pdf):
        today = date.today()
        format = today.strftime('%d/%m/%Y')
        archivo_imagen = settings.MEDIA_ROOT + '/msp.jpg'
        pdf.drawImage(archivo_imagen, 40, 720, 120, 90, preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(250, 790, 'Unidad Educativa')
        pdf.setFont('Helvetica', 14)
        pdf.drawString(240, 770, '"' 'Mis Primeros Pasos' '"')
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(230, 750, "REPORTE DE DOCENTES")
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(480, 770, format)
        pdf.line(470, 767, 560, 767)

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=A4)
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        # Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Usuario', 'Nombres', 'Apellidos', 'Cedula', 'Fecha de Registro')
        # Creamos una lista de tuplas que van a contener a las personas
        detalles = [(docente.username, docente.first_name, docente.last_name, docente.cedula,
                     docente.date_joined.strftime('%d/%m/%Y')) for docente in
                    Docente.objects.all()]
        width, height = A4
        # Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[3 * cm, 3 * cm, 3 * cm, 3.15 * cm])
        # Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                # La primera fila(encabezados) va a estar centrada
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                # Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                # El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        # Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, width, height)
        # Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 100, y)


