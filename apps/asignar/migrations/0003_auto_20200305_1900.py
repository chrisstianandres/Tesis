# Generated by Django 2.0.6 on 2020-03-06 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asignar', '0002_auto_20200305_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignar',
            name='docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='docente.Docente', unique=True),
        ),
    ]
