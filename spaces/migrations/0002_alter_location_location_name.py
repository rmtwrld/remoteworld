# Generated by Django 4.2.4 on 2023-08-15 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
