from django.db import models

SEXO = (
    (1, 'Masculino'),
    (0, 'Femenino'),
)

class Representante(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=20, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    correo = models.CharField(max_length=50, null=True, blank=True, unique=True)
    sexo = models.IntegerField(choices=SEXO, default=1)

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)

    class Meta:
        db_table = 'representante'
        verbose_name = 'representante'
        verbose_name_plural = 'representante'
        ordering = ['-nombres', '-cedula', '-apellidos']
