from ..curso.models import *
from ..docente.models import *
from ..silabo.models import *
from ..alumno.models import *
from ..asignar.models import *
from datetime import *
from ..lista.models import *
from django.contrib.auth.models import User

REGISTRO_ESTADO = (
    (1, 'Falta'), (2, 'Registrado')
)
REGISTRO_ASISTENCIA = (
    (1, 'Falta'), (2, 'Registrado')
)

class Horario(models.Model):
    #ciclo = models.IntegerField(choices=CICLO, default=1)
    hora_inicio = models.CharField(max_length=5)
    hora_fin = models.CharField(max_length=5)
    #listado = models.ForeignKey(Listado, on_delete=models.CASCADE, null=True, blank=True)
    #curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    asignar = models.ForeignKey(Asignar, on_delete=models.CASCADE, null=True, blank=True)
    #docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True, blank=True)
    silabo = models.ForeignKey(Silabo, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField(default=datetime.now)
    estado = models.IntegerField(choices=REGISTRO_ESTADO, default=1)
    asist_alum = models.IntegerField(choices=REGISTRO_ASISTENCIA, default=1)

    def __str__(self):
        return '%s'% (self.silabo.materia)
    def horas(self):
        return self.hora_inicio+' - '+self.hora_fin

    class Meta:
        db_table = 'horario'
        verbose_name = 'horario'
        verbose_name_plural = 'horarios'
        ordering = ['-id']

class Actividad(models.Model):
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, null=True, blank=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=150)
    observacion = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.id)

    class Meta:
        db_table = 'actividad'
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'
        ordering = ['-id']