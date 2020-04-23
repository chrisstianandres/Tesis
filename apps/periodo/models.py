
from django.db import models
from datetime import datetime
from django.utils.timezone import now


class Periodo(models.Model):

    periodo_inicio = models.DateField(default=datetime.now)
    periodo_fin = models.DateField(default=datetime.now)

    def __str__(self):
        return '%s %s %s' % (self.periodo_inicio.year, '-', self.periodo_fin.year)

    class Meta:
        db_table = 'periodo'
        verbose_name = 'periodo'
        verbose_name_plural = 'periodos'
        ordering = ['-periodo_inicio']

