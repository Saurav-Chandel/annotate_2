# Generated by Django 4.0.3 on 2022-04-29 12:34

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(upload_to=django.core.files.storage.FileSystemStorage(location='/media/photos')),
        ),
    ]
