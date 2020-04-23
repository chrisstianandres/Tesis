from django.contrib import admin
from .models import *

class HorarioAdmin(admin.TabularInline):
    model = Actividad

class ActividadAdmin(admin.ModelAdmin):
    inlines = (HorarioAdmin,)

admin.site.register(Horario,ActividadAdmin)