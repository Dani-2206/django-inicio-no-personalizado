# Generated by Django 3.2.3 on 2021-07-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colab',
            fields=[
                ('rut', models.IntegerField(max_length=10, primary_key=True, serialize=False, verbose_name='rut')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de usuario')),
                ('email', models.CharField(max_length=100, verbose_name='Correo Electronico')),
                ('telefono', models.CharField(max_length=9, verbose_name='Número de contacto')),
                ('pais', models.CharField(max_length=20, verbose_name='Pais')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('contraseña', models.CharField(max_length=35, verbose_name='Contraseña')),
            ],
        ),
    ]
