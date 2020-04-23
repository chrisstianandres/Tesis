from django.db import models
from ..horario.models import *
from ..lista.models import *
# Create your models here.
ASISTE = (
    (1, 'Presente'),
    (0, 'Falta'),
)

class Asistencias(models.Model):
    Horario = models.ForeignKey(Horario, on_delete=models.CASCADE, null=True, blank=True)
    Listado = models.ForeignKey(Listado, on_delete=models.CASCADE, null=True, blank=True)
    Asistencia= models.IntegerField(choices=ASISTE, default=0, null=True, blank=True)
    fecha= models.DateField(default=datetime.now, null=True, blank=True)
    def __str__(self):
        return '%s %s %s' % (self.Listado.alumno, self.Asistencia, self.fecha )

    class Meta:
        db_table = 'asistencia'
        verbose_name = 'asistencia'
        verbose_name_plural = 'asistencias'

