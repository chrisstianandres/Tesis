"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from apps import backEnd as backEnd
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from apps.notas.ajax import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', backEnd.logeo, name='login'),  # pagina_login
    url(r'^connect/$', backEnd.connect, name='connect'),  # logearse
    url(r'^disconnect/$', backEnd.disconnect, name='disconnect'),  # desconectarse
    url(r'^reset/password_reset', auth_views.password_reset,
        {'template_name': 'back-end/registration/password_reset_form.html', 'email_template_name':
            'back-end/registration/password_reset_email.html'}, name='password_reset'),
    url(r'^reset/password_done', auth_views.password_reset_done,
        {'template_name': 'back-end/registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm,
        {'template_name': 'back-end/registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done', auth_views.password_reset_complete,
        {'template_name': 'back-end/registration/password_reset_complete.html'}, name='password_reset_complete'),
    # SISTEMA
    url(r'^$', login_required(backEnd.menu), name='menu'),
    url(r'^horario_json/$', login_required(backEnd.horario_json), name='horario_json'),
    url(r'^horario_json_admin/$', login_required(backEnd.horario_json_admin), name='horario_json_admin'),
    url(r'^actividad_id/$', login_required(backEnd.actividad_id), name='horario_json'),
    url(r'^registrar_clase$', login_required(backEnd.registrar_clase), name='registrar_clase'),
    url(r'^asistencia_registrar$', login_required(backEnd.asistencia_registrar), name='asistencia_registrar'),
    url(r'^ajax/get_periodo/$', login_required(get_periodo), name='get_periodo'),
    url(r'^ajax/get_curso/$', login_required(get_curso), name='get_curso'),
    url(r'^ajax/get_fecha/$', login_required(get_fecha), name='get_fecha'),
    url(r'^ajax/get_curso_asistencias/$', login_required(get_curso_asistencias), name='get_curso_asistencias'),
    url(r'^ajax/get_materia/$', login_required(get_materia), name='get_materia'),
    url(r'^ajax/get_alumno/$', login_required(get_alumno), name='get_alumno'),
    url(r'^ajax/get_alumno_asistencias/$', login_required(get_alumno_asistencias), name='get_alumno_asistencias'),
    url(r'^ajax/get_parcial/$', login_required(get_parcial), name='get_parcial'),
    url(r'^ajax/get_notas/$', login_required(get_notas), name='get_notas'),
    url(r'^ajax/save_note/$', login_required(save_note), name='save_note'),

    url(r'^silabo/', include('apps.silabo.urls', namespace='silabos')),
    url(r'^periodo/', include('apps.periodo.urls', namespace='periodo')),
    url(r'^aula/', include('apps.aula.urls', namespace='aula')),
    url(r'^representante/', include('apps.representante.urls', namespace='representante')),
    url(r'^docente/', include('apps.docente.urls', namespace='docente')),
    url(r'^curso/', include('apps.curso.urls', namespace='curso')),
    url(r'^materia/', include('apps.materia.urls', namespace='materias')),
    url(r'^alumnos/', include('apps.alumno.urls', namespace='alumnos')),
    url(r'^matriculas/', include('apps.lista.urls', namespace='matriculas')),
    url(r'^asistencias/', include('apps.asistencias.urls', namespace='asistencia_list')),
    url(r'^horario/', include('apps.horario.urls', namespace='horario')),
    url(r'^asignar/', include('apps.asignar.urls', namespace='asignar')),
    url(r'^notas/', include('apps.notas.urls', namespace='notas')),
    url(r'^notas_net$', backEnd.notas, name='notas_net'),
    url(r'^alumnos_notas$', backEnd.notas_net, name='alumnos_notas'),
    url(r'^notas_alumnos$', backEnd.notas_alumnos, name='notas_alumnos'),
    # url(r'^materia/', include('apps.horario.urls', namespace='materia')),
    # url(r'^lista_mat_asit/', include('apps.horario.urls', namespace='lista_mat_asit')),
    # url(r'^asistencia/', include('apps.horario.urls', namespace='asistencia')),
    # url(r'^silabo2/', include('apps.horario.urls', namespace='silabolista1')),
    # url(r'^alumno/', include('apps.asistencias.urls', namespace='alumno_list')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
