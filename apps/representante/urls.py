from django.conf.urls import url
from . import views
from apps.representante.views import *
from django.contrib.auth.decorators import login_required
app_name = 'Representante'

urlpatterns = [
    #url(r'^listado$', Alumno_lista.as_view(), name='lista'),
    url(r'^nuevo', login_required(views.nuevo), name='nuevo'),
    url(r'^crear', login_required(views.crear), name='crear'),
    url(r'^editar/(?P<id_representante>\d+)/$', login_required(views.editar), name='editar'),
    url(r'^lista', login_required(views.listado), name='lista'),


]