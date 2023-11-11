# Generated by Django 3.2.22 on 2023-11-11 16:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0003_alter_todomodel_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 11, 16, 21, 33, 253413, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todomodel',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 11, 16, 21, 39, 923306, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
