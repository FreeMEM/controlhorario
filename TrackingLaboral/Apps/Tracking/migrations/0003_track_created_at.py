# Generated by Django 2.2.1 on 2019-05-25 15:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0002_auto_20190523_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
