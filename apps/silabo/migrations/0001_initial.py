# Generated by Django 2.0.6 on 2020-03-05 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Silabo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semana', models.IntegerField(default=1)),
                ('unidad', models.IntegerField(default=1)),
                ('clase', models.IntegerField(default=1)),
                ('tema', models.CharField(max_length=250)),
                ('materia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materia.Materia')),
            ],
            options={
                'verbose_name': 'silabo',
                'db_table': 'silabo',
                'verbose_name_plural': 'silabos',
                'ordering': ['-materia', '-semana', '-unidad', '-tema'],
            },
        ),
    ]
