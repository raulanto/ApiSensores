# Generated by Django 5.0.3 on 2024-09-09 03:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proceso', '0004_remove_etapa_duracion_en_horas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa',
            name='fkProceso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proceso.proceso', verbose_name='Proceso'),
        ),
    ]
