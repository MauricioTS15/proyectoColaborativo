# Generated by Django 4.1.7 on 2023-04-17 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProyectos', '0005_rename_tarea_realizar_proyecto_tareas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='nivel_prioridad',
            new_name='prioridad',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='notas_adicionales',
        ),
        migrations.AddField(
            model_name='tarea',
            name='notas',
            field=models.CharField(default='', max_length=255),
        ),
    ]
