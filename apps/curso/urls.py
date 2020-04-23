from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
app_name = 'Curso'
urlpatterns = [
    url(r'^cursos(?P<id_materia>\d+)/(?P<id_periodo>\d+)/$', login_required(views.curso_list), name='cursos'),
    url(r'^nuevo$', login_required(views.nuevo_curso), name='nuevo_curso'),
    url(r'^crear$', login_required(views.crear_curso), name='crea_curso'),
    url(r'^lista$', login_required(views.lista), name='lista'),
    url(r'^editar/(?P<id_curso>\d+)/$', login_required(views.editar), name='editar'),
    url(r'^eliminar$', login_required(views.eliminar), name='eliminar'),

]