# Generated by Django 4.1.7 on 2023-12-12 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_fun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribeduser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 12, 15, 32, 59, 725812, tzinfo=datetime.timezone.utc), verbose_name='Date Created'),
        ),
    ]
