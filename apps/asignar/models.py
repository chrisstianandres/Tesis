from django.db import models
from ..docente.models import *
from ..materia.models import *
from ..periodo.models import *
from ..curso.models import *
from datetime import datetime
from django.utils.timezone import now
ESTADO = (
    (0, 'Activo'),
    (1, 'Retirado'),
    (2, 'Suspendido'),
)

class Asignar(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True, blank=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.IntegerField(choices=ESTADO, default=0)

    def __str__(self):
        return '%s %s %s' % (self.docente, self.materia.nombre, self.periodo)

    class Meta:
        db_table = 'asignar'
        verbose_name = 'asignar'
        verbose_name_plural = 'asignaciones'


