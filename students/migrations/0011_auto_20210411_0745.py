# Generated by Django 3.1.7 on 2021-04-11 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20210410_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
