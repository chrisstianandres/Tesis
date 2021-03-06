# Generated by Django 2.0.6 on 2020-03-25 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quimestre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parcial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=1, unique=True)),
                ('quimestre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quimestre.Quimestre')),
            ],
            options={
                'db_table': 'parcial',
                'verbose_name': 'parcial',
                'verbose_name_plural': 'parciales',
            },
        ),
    ]
