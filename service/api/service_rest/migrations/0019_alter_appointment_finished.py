# Generated by Django 4.0.3 on 2022-10-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0018_alter_appointment_date_alter_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]