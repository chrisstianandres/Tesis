from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from apps.asignar.views import *
app_name = 'Asignar'

urlpatterns = [
    url(r'^nuevo/(?P<id_docente>\d+)/$', login_required(views.nuevo), name='nuevo'),
    url(r'^get_datos', login_required(views.get_datos), name='get_datos'),
    url(r'^crear', login_required(views.crear), name='crear'),
    url(r'^listado', login_required(views.Lista_Asignadas), name='listado'),
    url(r'^lista_asignadas', login_required(views.Lista_Asignadas_docente), name='lista_asignadas'),
    url(r'^lista_cursos/(?P<id_curso>\d+)/(?P<id_periodo>\d+)/$', login_required(views.Lista_cursos), name='lista_cursos'),
    url(r'^asignadas/(?P<id_docente>\d+)/$', login_required(views.Lista_Asignadas_admin), name='asignadas'),
    url(r'^editar/(?P<id_asignar>\d+)/$', login_required(views.editar), name='editar'),



]