# Generated by Django 3.2.18 on 2023-04-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ehr',
            name='address',
        ),
        migrations.RemoveField(
            model_name='ehr',
            name='phone',
        ),
        migrations.AddField(
            model_name='ehr',
            name='ehr_status',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='ehr',
            name='age',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='ehr',
            name='document',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='ehr',
            name='gender',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='ehr',
            name='patient_fname',
            field=models.CharField(default='', max_length=20),
        ),
    ]
