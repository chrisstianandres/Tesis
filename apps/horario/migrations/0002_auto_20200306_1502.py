# Generated by Django 2.0.6 on 2020-03-06 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='hora_inicio',
            field=models.TimeField(),
        ),
    ]
