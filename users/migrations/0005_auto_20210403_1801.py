# Generated by Django 3.1.3 on 2021-04-03 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favorite',
        ),
    ]
