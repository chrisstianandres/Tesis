from django.db import models

class Quimestre(models.Model):
    numero = models.IntegerField(unique=True)

    def __str__(self):
        return '%s %s %s' % ("Quimestre", "", self.numero)

    class Meta:
        db_table = 'quimestre'
        verbose_name = 'quimestre'
        verbose_name_plural = 'quimestres'




