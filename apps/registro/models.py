from ..horario.models import *

class Registro(models.Model):
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, null=True, blank=True)
    fecha_registro = models.DateTimeField('Created Time', auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.id, self.fecha_registro)

    class Meta:
        db_table = 'registro'
        verbose_name = 'registro'
        verbose_name_plural = 'registros'
        ordering = ['-id']
