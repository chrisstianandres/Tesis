from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from apps.periodo.views import *
app_name = 'Periodos'

urlpatterns = [
    url(r'^listado$', login_required(views.listado), name='listado'),
    url(r'^nuevo', login_required(views.nuevo), name='nuevo'),
    url(r'^crear', login_required(views.crear), name='crear'),
    url(r'^editar/(?P<id_periodo>\d+)/$', login_required(views.editar), name='editar'),
    url(r'^eliminar$', login_required(views.eliminar), name='eliminar'),

]