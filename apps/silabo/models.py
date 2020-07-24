from ..materia.models import *

class Silabo(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True, blank=True)
    semana = models.IntegerField(default=1)
    unidad = models.IntegerField(default=1)
    clase = models.IntegerField(default=1)
    tema = models.CharField(max_length=250)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.materia, 'Semana',  self.semana,  'Unidad', self.unidad,  'Clase',
                                               self.clase,  'Tema', self.tema)

    class Meta:
        db_table = 'silabo'
        verbose_name = 'silabo'
        verbose_name_plural = 'silabos'
        ordering = ['-materia', '-semana', '-unidad', '-tema', '-clase']

