from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'Asistencias'
urlpatterns = [
    #url(r'^alumno_list$', login_required(views.alumno_list), name='alumno_list'),
    #url(r'^alumno_list2$', login_required(views.alumno_list2), name='alumno_list2'),
    url(r'^asistencia$', login_required(views.vista_asistencias), name='asistencia'),
    url(r'^asistencia_report$', login_required(views.get_asistencias), name='asistencia_report'),
    url(r'^save_asistencia$', login_required(views.save_asistencia), name='save_asistencia'),

]
