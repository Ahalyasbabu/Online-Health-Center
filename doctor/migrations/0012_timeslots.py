# Generated by Django 3.2.18 on 2023-03-01 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_delete_timeslots'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeSlot', models.CharField(max_length=20)),
                ('dateSlot', models.CharField(max_length=10)),
                ('availability', models.CharField(max_length=10)),
                ('doctorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.docotrs')),
            ],
        ),
    ]