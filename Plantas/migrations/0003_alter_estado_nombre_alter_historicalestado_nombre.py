# Generated by Django 5.0.3 on 2024-04-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plantas', '0002_historicalplanta_organizacion_planta_organizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='historicalestado',
            name='nombre',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]