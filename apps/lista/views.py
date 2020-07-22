from django.shortcuts import render, redirect
from .models import *
from apps.lista.models import Listado
from django.urls import reverse_lazy
from django.views.generic import *
from apps.lista.forms import ListadoForm
from django.http import *
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape, letter
from reportlab.lib.units import inch, mm, cm
from reportlab.lib.fonts import *
from django.views.generic import ListView
from reportlab.lib import colors
from reportlab.platypus import TableStyle, Table, Paragraph
from datetime import date
from reportlab.lib.styles import (ParagraphStyle, getSampleStyleSheet)

from reportlab.lib.enums import TA_CENTER

opc_icono = 'fa fa-address-card-o'
opc_ruta = '/matriculas/'
opc_nuevo = '/matriculas/nuevo'
opc_crud = '/matriculas/crear/'
opc_delete = '/matriculas/borrar'
opc_entidad = 'Matriculas'


def nuevo(request):
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
        'boton': 'Guardar Matricula', 'action': 'add', 'titulo': 'Nuevo Registro de Matricula',
    }
    if request.method == 'GET':
        data['form'] = ListadoForm()
    return render(request, 'back-end/listado/listado_form.html', data)


def crear(request):
    f = ListadoForm(request.POST)
    data = {
        'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud
    }
    action = request.POST['action']
    data['action'] = action
    alumno = request.POST.get('alumno')
    periodo = request.POST.get('periodo')
    curso = request.POST.get('curso')
    if request.method == 'POST' and 'action' in request.POST:
        if Listado.objects.filter(alumno=alumno, periodo=periodo):
            f = ListadoForm(request.POST)
            a = Alumno.objects.get(id=alumno)
            p = Periodo.objects.get(id=periodo)
            data = {
                'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
                'boton': 'Guardar Matricula', 'action': 'add', 'titulo': 'Nuevo Registro de Matricula',
                'form': f, 'errorrep': 'Ya existe una matricula para '+ str(a)+ "en el periodo " + str(p)
            }
        else:

            if f.is_valid():
                f.save()
                a = Alumno.objects.get(id=alumno)
                a.estado = 0
                a.save()
            else:
                data = {
                    'icono': opc_icono, 'ruta': opc_ruta, 'crud': opc_crud, 'entidad': opc_entidad,
                    'boton': 'Guardar Matricula', 'action': 'add', 'titulo': 'Nuevo Registro de Matricula',
                    'form': f
                }
                return render(request, 'back-end/listado/listado_form.html', data)
            return HttpResponseRedirect('/matriculas/lista')
        return render(request, 'back-end/listado/listado_form.html', data)


def reporte(request, id_lista):
    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=landscape(letter))
    today = date.today()
    format = today.strftime('%d/%m/%Y')
    archivo_imagen = settings.MEDIA_ROOT + '/msp.jpg'
    pdf.drawImage(archivo_imagen, 25, 500, 120, 90, preserveAspectRatio=True)
    pdf.setFont("Helvetica-Bold", 30)
    pdf.drawString(270, 550, 'Unidad Educativa')
    pdf.setFont('Helvetica', 25)
    pdf.drawString(280, 520, '"' 'Mis Primeros Pasos' '"')
    pdf.setFont("Helvetica-Bold", 40)
    pdf.drawString(80, 450, "COMPROBANTE DE MATRICULA")
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(10 * cm, 80, "Cpa. Yolanda Maldonado Bastidas")
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(13 * cm, 65, "Directora")
    pdf.line(9 * cm, 100, 19 * cm, 100)
    pdf.setFillColor("red")
    pdf.setFont("Helvetica-Bold", 18)

    pdf.drawString(690, 550, format)
    y = 250
    encabezados = ('Alumno', 'Cédula', 'Curso', 'Periodo', 'Representante ', 'Fecha')
    # Creamos una lista de tuplas que van a contener a las personas
    detalles = []
    styles = getSampleStyleSheet()
    yourStyle = ParagraphStyle('yourtitle',
                               valing='MIDDLE',
                               fontSize=16,
                               alignment=0,
                               leading=18,
                               borderPadding=(2, 2, 2, 2)
                               )
    # [(matricula.alumno, matricula.alumno.cedula, matricula.curso, matricula.periodo,
    #   matricula.fecha.strftime('%d/%m/%Y'))
    for matricula in Listado.objects.filter(id=id_lista):
        p = Paragraph(str(matricula.alumno), yourStyle)
        r = Paragraph(str(matricula.alumno.representante), yourStyle)
        detalles.append((p, matricula.alumno.cedula, matricula.curso.nombre, matricula.periodo, r,
                         matricula.fecha.strftime('%d/%m/%Y')))
    # lista_nombres = []
    # for var in Listado.objects.filter(id=id_lista):
    #   lista_nombres.append((var.alumno, var.curso, var.periodo))

    # print(lista_nombres)
    width, height = A4
    # Establecemos el tamaño de cada una de las columnas de la tabla
    detalle_orden = Table([encabezados] + detalles, colWidths=[5 * cm, 3.5 * cm, 3.5 * cm, 3.5 * cm, 5.5 * cm, 3 * cm],
                          rowHeights=[1.5 * cm, 1.5 * cm])
    # Aplicamos estilos a las celdas de la tabla
    detalle_orden.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('BOX', (0, 0), (-1, -1), 2, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
            ('ALIGN', (0, 0), (5, 0), 'CENTER'),
            ('ALIGN', (1, 1), (5, 1), 'CENTER'),
            ('FONTSIZE', (0, 0), (5, 0), 18),
            ('FONTSIZE', (0, 1), (5, 1), 16),
            ('FONTNAME', (0, 0), (5, 0), 'Courier-Bold'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]
    ))
    # Establecemos el tamaño de la hoja que ocupará la tabla
    detalle_orden.wrapOn(pdf, width, height)
    # Definimos la coordenada donde se dibujará la tabla
    detalle_orden.drawOn(pdf, 75, y)
    pdf.showPage()
    pdf.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def Matriculas_lista(request):
    matriculas_list = Listado.objects.filter(estado=0)
    contexto = {'matriculas_list': matriculas_list}
    return render(request, "back-end/listado/listado.html", contexto)

