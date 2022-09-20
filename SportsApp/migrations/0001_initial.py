# Generated by Django 4.1 on 2022-09-20 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('numeroIntegrantes', models.IntegerField()),
                ('deporte', models.CharField(max_length=20)),
                ('fechaFundacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Facilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('posicion', models.CharField(max_length=20)),
            ],
        ),
    ]