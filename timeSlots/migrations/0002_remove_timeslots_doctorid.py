# Generated by Django 3.2.18 on 2023-03-01 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeSlots', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslots',
            name='doctorId',
        ),
    ]