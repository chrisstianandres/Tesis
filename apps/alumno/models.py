from django.db import models
from ..representante.models import *

SEXO = (
    (1, 'Masculino'),
    (0, 'Femenino'),
)
ESTADO = (
    (0, 'Activo'), (1, 'Retirado'), (2, 'Suspendido'), (3, 'Inactivo')
)

class Alumno(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=20, null=True, blank=True)
    cedula = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    representante = models.ForeignKey(Representante, on_delete=models.CASCADE, null=True, blank=True)
    correo = models.CharField(max_length=50, null=True, blank=True, unique=True)
    sexo = models.IntegerField(choices=SEXO, default=1)
    estado = models.IntegerField(choices=ESTADO, default=3, blank=True, null=True)


    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)

    class Meta:
        db_table = 'alumno'
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'
        ordering = ['-nombres', '-cedula', '-apellidos']
