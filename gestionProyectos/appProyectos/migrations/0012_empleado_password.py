# Generated by Django 4.1.7 on 2023-05-11 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProyectos', '0011_remove_proyecto_tareas_tarea_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='password',
            field=models.CharField(default='', max_length=155),
        ),
    ]
