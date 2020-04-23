from django.db import models

class Aula(models.Model):
    numero = models.IntegerField(default=1, unique=True)

    def __str__(self):
        return '%s' % (self.numero)

    class Meta:
        db_table = 'aula'
        verbose_name = 'aula'
        verbose_name_plural = 'aulas'
        ordering = ['-numero']

