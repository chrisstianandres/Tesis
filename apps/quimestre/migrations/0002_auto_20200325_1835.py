# Generated by Django 2.0.6 on 2020-03-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quimestre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quimestre',
            name='numero',
            field=models.IntegerField(unique=True),
        ),
    ]
