from ..aula.models import *
ESTADO = (
    (0, 'Matutino'), (1, 'Vespertino')
)

class Curso(models.Model):
    nombre = models.CharField(max_length=25, unique=True)
    seccion = models.IntegerField(choices=ESTADO, default=0, null=True, blank=True)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):

        return '%s %s %s' % (self.nombre, " - ", self.seccion)
    class Meta:
        db_table = 'curso'
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering = ['-nombre', '-aula']

