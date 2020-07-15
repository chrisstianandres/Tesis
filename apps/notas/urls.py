from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from apps.notas.ajax import get_curso, get_materia
app_name = 'Notas'
urlpatterns = [
   url(r'^alumnos$', login_required(views.vista_notas_request), name='alumnos'),
   url(r'^notas$', login_required(views.vista_notas), name='notas'),
   url(r'^notas_curso$', login_required(views.vista_notas_curso), name='notas_curso'),
   url(r'^notas_curso_materias/(?P<alumno>\d+)/(?P<periodo>\d+)$', login_required(views.vista_notas_curso_materias),
       name='notas_curso_materias'),
]
