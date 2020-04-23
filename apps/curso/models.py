from ..aula.models import *

class Curso(models.Model):
    nombre = models.CharField(max_length=25, unique=True)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):

        return '%s' % (self.nombre)
    class Meta:
        db_table = 'curso'
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering = ['-nombre', '-aula']

