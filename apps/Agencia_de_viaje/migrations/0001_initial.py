# Generated by Django 3.2.7 on 2021-09-27 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia_de_viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=45)),
                ('Telefono', models.CharField(max_length=15)),
                ('Ciudad', models.CharField(max_length=20)),
            ],
        ),
    ]