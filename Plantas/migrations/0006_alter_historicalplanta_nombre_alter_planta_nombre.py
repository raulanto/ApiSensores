# Generated by Django 5.0.3 on 2024-04-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plantas', '0005_alter_historicalplanta_nombre_alter_planta_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalplanta',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='planta',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
