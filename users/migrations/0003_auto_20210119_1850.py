# Generated by Django 3.1.5 on 2021-01-19 18:50

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=django.contrib.gis.geos.point.Point(2.351462, 48.856697), max_length=40, null=True, srid=4326),
        ),
        migrations.CreateModel(
            name='MatchedUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_user_1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_user_2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
