# Generated by Django 3.2.7 on 2021-11-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserva', '0002_alter_reserva_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='Fecha_ingreso',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='Fecha_salida',
            field=models.DateTimeField(),
        ),
    ]
