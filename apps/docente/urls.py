from django.conf.urls import url
from apps.docente import views
from apps.docente.views import *
from django.contrib.auth.decorators import login_required

app_name = 'Docente'
urlpatterns = [
    url(r'^menu2$', login_required(views.menu), name='menu_docente'),
    url(r'^nuevo$', login_required(views.nuevo), name='nuevo'),
    url(r'^crear', login_required(views.crear), name='crear'),
    url(r'^editar/(?P<id_docente>\d+)/$', login_required(views.editar), name='editar'),
    url(r'^listado$', login_required(views.Docente_list), name='Docente_list'),
    url(r'^estado$', login_required(views.estado), name='estado'),
    url(r'^reporte_docentes_pdf/$', login_required(ReportePersonasPDF.as_view()), name="reporte_docentes_pdf"),
    url(r'^profile/$', login_required(views.profile), name="reporte_docentes_pdf"),
    ]