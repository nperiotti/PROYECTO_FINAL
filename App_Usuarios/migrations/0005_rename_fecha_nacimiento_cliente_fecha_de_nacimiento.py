# Generated by Django 5.2.4 on 2025-08-01 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Usuarios', '0004_rename_telefono_cliente_telefono'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='fecha_nacimiento',
            new_name='fecha_de_nacimiento',
        ),
    ]
