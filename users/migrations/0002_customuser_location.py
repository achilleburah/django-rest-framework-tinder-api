# Generated by Django 3.1.5 on 2021-01-19 14:22

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(max_length=40, null=True, srid=4326),
        ),
    ]
