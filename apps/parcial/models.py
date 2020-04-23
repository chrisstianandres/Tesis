from django.db import models
from apps.quimestre.models import *

class Parcial(models.Model):
    quimestre= models.ForeignKey(Quimestre, on_delete=models.CASCADE, null=True, blank=True)
    numero = models.IntegerField()

    def __str__(self):
        return '%s %s %s %s %s' % (self.quimestre, "", "Parcial ", "", self.numero)

    class Meta:
        db_table = 'parcial'
        verbose_name = 'parcial'
        verbose_name_plural = 'parciales'


