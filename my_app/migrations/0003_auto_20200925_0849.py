# Generated by Django 2.2.6 on 2020-09-25 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20200925_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewed_messages',
            name='sms_notification',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
