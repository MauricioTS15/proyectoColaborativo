# Generated by Django 4.1.7 on 2023-04-18 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appProyectos', '0006_rename_nivel_prioridad_tarea_prioridad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Prioridad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=155)),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=155),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=155),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=155),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(max_length=9),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='apellido',
            field=models.CharField(max_length=155),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.EmailField(max_length=155),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(max_length=155),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.IntegerField(max_length=9),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(max_length=155),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='nombre',
            field=models.CharField(max_length=155),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='notas',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProyectos.estado'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='prioridad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProyectos.prioridad'),
        ),
    ]
