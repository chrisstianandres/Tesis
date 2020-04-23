from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'Silabo'
urlpatterns = [
    url(r'^nuevo$', login_required(views.nuevo), name='nuevo'),
    url(r'^guardar$', login_required(views.save_silabo), name='guardar'),
    url(r'^listado$', login_required(views.silabo_list), name='lista'),
    url(r'^editar/(?P<id>\d+)/$', login_required(views.editar), name='editar'),
    url(r'^get_silabo$', login_required(views.get_silabo), name='get_silabo'),
    url(r'^get_last_silabo$', login_required(views.get_last_silabo), name='get_last_silabo'),
    url(r'^eliminar$', login_required(views.eliminar), name='eliminar'),
]