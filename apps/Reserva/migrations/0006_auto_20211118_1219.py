# Generated by Django 3.2.7 on 2021-11-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserva', '0005_auto_20211118_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='Fecha_ingreso',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='Fecha_salida',
            field=models.DateField(),
        ),
    ]