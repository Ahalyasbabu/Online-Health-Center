# Generated by Django 3.2.18 on 2023-02-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_docotrs_year_of_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='docotrs',
            name='departments_id',
            field=models.CharField(default=None, max_length=10),
        ),
    ]