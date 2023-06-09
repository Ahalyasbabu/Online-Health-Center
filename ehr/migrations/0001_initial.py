# Generated by Django 3.2.18 on 2023-04-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EHR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_fname', models.CharField(max_length=20)),
                ('patient_lname', models.CharField(default='', max_length=20)),
                ('age', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('document', models.CharField(max_length=30)),
                ('email', models.CharField(default='default', max_length=20)),
            ],
        ),
    ]
