from django.db import models

class Materia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        db_table = 'materia'
        verbose_name = 'materia'
        verbose_name_plural = 'materias'
        ordering = ['-nombre']

