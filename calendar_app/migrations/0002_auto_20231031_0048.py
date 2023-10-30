# Generated by Django 3.2.22 on 2023-10-30 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='duedate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('primary', '完了'), ('warning', '着手'), ('dangar', '未着手'), ('dark', '期限切れ')], default='dangar', max_length=50),
            preserve_default=False,
        ),
    ]
