# Generated by Django 4.0.3 on 2022-10-25 20:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0003_rename_tech_appointment_technician'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='scheduled_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
