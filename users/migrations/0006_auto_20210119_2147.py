# Generated by Django 3.1.5 on 2021-01-19 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_matchrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchrequest',
            old_name='asker',
            new_name='sender',
        ),
    ]
