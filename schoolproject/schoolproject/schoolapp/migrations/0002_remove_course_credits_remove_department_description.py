# Generated by Django 4.2.7 on 2023-11-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='credits',
        ),
        migrations.RemoveField(
            model_name='department',
            name='description',
        ),
    ]
