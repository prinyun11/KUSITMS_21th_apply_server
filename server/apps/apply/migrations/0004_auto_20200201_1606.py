# Generated by Django 3.0.2 on 2020-02-01 16:06

import apps.apply.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0003_snsimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyform',
            name='image',
            field=models.ImageField(upload_to=apps.apply.models.get_image_name),
        ),
    ]
