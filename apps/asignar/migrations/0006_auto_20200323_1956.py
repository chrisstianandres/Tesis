# Generated by Django 2.0.6 on 2020-03-23 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0011_auto_20200323_1956'),
        ('asignar', '0005_asignar_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignar',
            name='curso',
        ),
        migrations.AddField(
            model_name='asignar',
            name='listado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lista.Listado'),
        ),
    ]
