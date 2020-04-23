from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
app_name = 'Horario'
urlpatterns = [
    url(r'^nuevo_admin$', login_required(views.nuevo_admin), name='nuevo_admin'),
    url(r'^nuevo$', login_required(views.nuevo), name='nuevo'),
    url(r'^get_periodo$', login_required(views.get_periodo), name='get_periodo'),
    url(r'^get_materia$', login_required(views.get_materia), name='get_materia'),
    url(r'^get_curso$', login_required(views.get_curso), name='get_curso'),
    url(r'^get_silabo$', login_required(views.get_silabo), name='get_silabo'),
    url(r'^save_horario$', login_required(views.save_horario), name='save_horario'),
    url(r'^get_alumno$', login_required(views.get_alumno), name='get_alumno'),
    url(r'^get_periodo_2$', login_required(views.get_periodo_2), name='get_periodo_2'),
    url(r'^get_materia_2$', login_required(views.get_materia_2), name='get_materia_2'),
    url(r'^get_curso_2$', login_required(views.get_curso_2), name='get_curso_2'),
    url(r'^save_horario_2$', login_required(views.save_horario_2), name='save_horario_2'),
    url(r'^ver$', login_required(views.horario_list), name='ver'),
    url(r'^horarios_admin$', login_required(views.horario_list_admin), name='horarios_admin'),
    url(r'^editar_admin/(?P<id>\d+)/$', login_required(views.editar), name='editar_admin'),
]