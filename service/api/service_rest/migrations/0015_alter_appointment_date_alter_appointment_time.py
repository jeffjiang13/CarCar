# Generated by Django 4.0.3 on 2022-10-27 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0014_remove_appointment_automobile_appointment_vin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]