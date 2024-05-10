# Generated by Django 5.0.4 on 2024-05-10 00:03

import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=utils.FileUpload.upload_to),
        ),
    ]
