# Generated by Django 3.1.7 on 2021-04-09 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_remove_staff_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='photo',
            field=models.ImageField(default=1, upload_to='media1/'),
            preserve_default=False,
        ),
    ]