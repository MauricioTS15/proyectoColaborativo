# Generated by Django 4.1.7 on 2023-05-11 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appProyectos', '0012_empleado_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='password',
        ),
    ]
