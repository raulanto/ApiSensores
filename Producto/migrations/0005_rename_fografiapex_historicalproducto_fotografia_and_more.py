# Generated by Django 5.0.3 on 2024-05-04 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0004_historicalproducto_etapa_producto_etapa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalproducto',
            old_name='fografiaPex',
            new_name='fotografia',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='fografiaPex',
            new_name='fotografia',
        ),
    ]
