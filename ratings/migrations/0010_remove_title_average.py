# Generated by Django 2.2.7 on 2019-11-24 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0009_auto_20191123_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='average',
        ),
    ]
