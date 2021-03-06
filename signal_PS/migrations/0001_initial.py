# Generated by Django 2.2.6 on 2020-12-07 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_app', '0006_auto_20201207_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControllerType',
            fields=[
                ('type', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SignalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30, unique=True)),
                ('boolean_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SignalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=12, unique=True, verbose_name='тип')),
                ('inversion', models.BooleanField(verbose_name='инверсия')),
            ],
        ),
        migrations.CreateModel(
            name='Voltage',
            fields=[
                ('value', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='напряжение')),
            ],
            options={
                'verbose_name_plural': 'Напряжение',
            },
        ),
        migrations.CreateModel(
            name='SimCardNumber',
            fields=[
                ('number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signal_PS.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='GsmController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50)),
                ('add_description', models.TextField()),
                ('number_SIM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signal_PS.SimCardNumber')),
                ('ps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Ps')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signal_PS.ControllerType')),
            ],
        ),
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='наименование')),
                ('date_up', models.DateTimeField(verbose_name='обновлено')),
                ('ps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Ps', verbose_name='пс')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signal_PS.SignalStatus', verbose_name='статус')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signal_PS.SignalType', verbose_name='тип')),
                ('voltage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='signal_PS.Voltage', verbose_name='напряжение')),
            ],
            options={
                'verbose_name_plural': 'Сигналы',
                'unique_together': {('type', 'voltage', 'name', 'ps')},
            },
        ),
    ]
