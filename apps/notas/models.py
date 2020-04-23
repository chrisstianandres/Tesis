from django.db import models
from ..asistencias.models import *
from ..asignar.models import *
from ..lista.models import *

class Notas(models.Model):
    #Asistencias = models.ForeignKey(Asistencias, on_delete=models.CASCADE, null=True, blank=True)
    Asignar = models.ForeignKey(Asignar, on_delete=models.CASCADE, null=True, blank=True)
    Listado = models.ForeignKey(Listado, on_delete=models.CASCADE, null=True, blank=True)
    #Quimestre_1 = models.IntegerField(default=1)
    Parcial_1_q_1 = models.FloatField(default=1)
    Parcial_2_q_1 = models.FloatField(default=0)
    Parcial_3_q_1 = models.FloatField(default=0)
    #Quimestre_2 = models.IntegerField(default=1)
    Parcial_1_q_2 = models.FloatField(default=0)
    Parcial_2_q_2 = models.FloatField(default=0)
    Parcial_3_q_2 = models.FloatField(default=0)
    examen_final = models.FloatField(default=0)

    def _get_quimestre_1(self):
        suma = (self.Parcial_1_q_1 + self.Parcial_2_q_1 + self.Parcial_3_q_1)/3
        return round(float(suma))
    Quimestre_1 = property(_get_quimestre_1)


    def _get_quimestre_2(self):
         suma=(int(self.Parcial_1_q_2) + int(self.Parcial_2_q_2) + int(self.Parcial_3_q_2))/3
         return round(float(suma))
    Quimestre_2 = property(_get_quimestre_2)


    def _get_nota(self):
        sum = int(self.Quimestre_1) + int(self.Quimestre_2)
        prom = sum/2
        if prom < 7:
            return (prom + self.examen_final) / 2
        else:
            return round(prom)
    Nota_final = property(_get_nota)


    def __str__(self):
        #format(Decimal.from_float(self.Parcial_1_q_1), '.2')
        return '%s, %s, %s' % (self.Listado.alumno, self.Asignar.materia, self.Nota_final)


    class Meta:
        db_table = 'notas'
        verbose_name = 'notas'
        verbose_name_plural = 'notas'

