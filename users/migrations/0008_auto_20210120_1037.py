# Generated by Django 3.1.5 on 2021-01-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210119_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchedusers',
            name='matches',
        ),
        migrations.RemoveField(
            model_name='matchedusers',
            name='owner',
        ),
        migrations.AddField(
            model_name='matchedusers',
            name='user1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matchedusers',
            name='user2',
            field=models.IntegerField(null=True),
        ),
    ]
