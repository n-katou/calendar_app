# Generated by Django 3.2.22 on 2023-10-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0002_auto_20231031_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('primary', '完了'), ('warning', '着手'), ('danger', '未着手'), ('dark', '期限切れ')], max_length=50),
        ),
    ]
