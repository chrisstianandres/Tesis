from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from apps.materia.views import *

app_name = 'Aulas'
urlpatterns = [
    url(r'^listado$', login_required(views.aula_list), name='lista'),
    url(r'^nuevo$', login_required(views.nuevo), name='nuevo'),
    url(r'^crear$', login_required(views.crear), name='crear'),
    url(r'^editar/(?P<id_aula>\d+)/$', login_required(views.editar), name='editar'),
    url(r'^eliminar$', login_required(views.eliminar), name='eliminar'),
]