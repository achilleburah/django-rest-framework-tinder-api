# Generated by Django 3.1.5 on 2021-01-20 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210120_1037'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MatchedUsers',
            new_name='MatchedUser',
        ),
    ]
