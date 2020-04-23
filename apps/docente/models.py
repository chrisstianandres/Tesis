from django.db import models
from django.contrib.auth.models import User

ROL = (
    (0, 'Admin'), (1, 'Docente')
)
ESTADO = (
    (0, 'Activo'), (1, 'Retirado'), (2, 'Suspendido')
)

class Docente(User):
    avatar = models.ImageField(upload_to='docente/%Y/%m/%d')#, default='docente/avatar.png')
    cedula = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=500, blank=True, null=True)
    rol = models.IntegerField(choices=ROL, default=1)
    estado = models.IntegerField(choices=ESTADO, default=0, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.get_full_name())

    class Meta:
        db_table = 'docente'
        verbose_name = 'docente'
        verbose_name_plural = 'docentes'
        ordering = ['-cedula']

