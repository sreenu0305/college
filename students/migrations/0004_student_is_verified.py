# Generated by Django 3.1.7 on 2021-04-05 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_staff_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
