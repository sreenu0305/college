# Generated by Django 3.1.7 on 2021-04-09 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20210408_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='photo',
        ),
    ]
