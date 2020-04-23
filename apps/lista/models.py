from django.db import models
from ..curso.models import *
from ..alumno.models import *
from ..periodo.models import *
from datetime import *
from django.utils.timezone import now

ESTADO = (
    (0, 'Matriculado'), (1, 'Retirado'), (2, 'Suspendido'), (3, 'Finalizado')
)

class Listado(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, null=True, blank=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField(default=now)
    estado = models.IntegerField(choices=ESTADO, default=0, blank=True, null=True)

    def __str__(self):
        return '%s' '%s' '%s' '%s' '%s' '%s' % (self.alumno, "  ", " Fecha ", self.fecha, "  ", self.periodo)

    class Meta:
        db_table = 'listado'
        verbose_name = 'listado'
        verbose_name_plural = 'listados'
        ordering = ['-periodo']
