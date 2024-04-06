# Generated by Django 5.0.3 on 2024-04-02 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valoresproductos',
            name='productos',
        ),
        migrations.AddField(
            model_name='valoresproductos',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='Producto.producto'),
        ),
    ]
