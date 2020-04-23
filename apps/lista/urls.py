from django.conf.urls import url
from  . import views
from apps.lista.views import *
from django.contrib.auth.decorators import login_required
app_name = 'Listado'

urlpatterns = [
    url(r'^nuevo', login_required(views.nuevo), name='nuevo'),
    url(r'^crear', login_required(views.crear), name='crear'),
    url(r'^lista/$', login_required(views.Matriculas_lista), name='lista'),
    url(r'^reporte/(?P<id_lista>\d+)/$', login_required(views.reporte), name='reporte'),
]