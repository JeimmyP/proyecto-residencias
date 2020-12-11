# Generated by Django 3.1.3 on 2020-12-11 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=300)),
                ('unidad', models.CharField(default='', max_length=100)),
                ('tipo', models.CharField(default='', max_length=50)),
                ('grupo', models.CharField(default='', max_length=100)),
                ('serie', models.CharField(default='', max_length=300)),
                ('parte', models.CharField(default='', max_length=150)),
                ('precio', models.CharField(default='', max_length=100)),
                ('toxico', models.CharField(default='', max_length=100)),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('tipo', models.CharField(default='', max_length=50)),
                ('cantidad', models.IntegerField(default='0')),
                ('importe', models.CharField(default='', max_length=100)),
                ('aplicacion', models.CharField(default='', max_length=100)),
                ('referencia', models.CharField(default='', max_length=500)),
                ('articuloId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.articulo')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='familiaId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.familia'),
        ),
    ]