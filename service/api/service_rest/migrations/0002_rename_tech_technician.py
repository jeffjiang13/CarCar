# Generated by Django 4.0.3 on 2022-10-25 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tech',
            new_name='Technician',
        ),
    ]
