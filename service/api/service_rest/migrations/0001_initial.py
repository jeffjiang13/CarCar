# Generated by Django 4.0.3 on 2022-10-25 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutomobileVO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('year', models.PositiveSmallIntegerField()),
                ('vin', models.CharField(max_length=17, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('reason', models.TextField(max_length=100)),
                ('finished', models.BooleanField()),
                ('canceled', models.BooleanField(default=False)),
                ('vip', models.BooleanField(default=False)),
                ('automobile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service', to='service_rest.automobilevo')),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service', to='service_rest.tech')),
            ],
        ),
    ]