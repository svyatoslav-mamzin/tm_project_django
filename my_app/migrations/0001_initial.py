# Generated by Django 2.2.6 on 2020-09-23 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ps',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('tel_number', models.CharField(max_length=12)),
                ('res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Sms_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=12)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('text_sms', models.TextField()),
                ('ps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Ps')),
            ],
        ),
        migrations.CreateModel(
            name='Viewed_messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_view', models.NullBooleanField()),
                ('datetime_view', models.DateTimeField(blank=True, null=True)),
                ('sms_notification', models.NullBooleanField()),
                ('id_SMS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Sms_message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.NullBooleanField()),
                ('phone_num_for_notif', models.CharField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
