# Generated by Django 2.2.1 on 2019-06-01 15:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0005_auto_20190530_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 15, 45, 38, 681692, tzinfo=utc)),
        ),
    ]
