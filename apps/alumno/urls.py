from django.conf.urls import url
from  . import views
from apps.alumno.views import *
from django.contrib.auth.decorators import login_required
app_name = 'Alumnos'

urlpatterns = [
    url(r'^listado$', login_required(Alumno_lista.as_view()), name='lista'),
    url(r'^nuevo', login_required(views.nuevo), name='nuevo'),
    url(r'^crear', login_required(views.crear), name='crear'),
    url(r'^editar/(?P<id_alumno>\d+)/$', login_required(views.editar), name='editar'),
    url(r'^estado$', login_required(views.estado), name='estado'),
]