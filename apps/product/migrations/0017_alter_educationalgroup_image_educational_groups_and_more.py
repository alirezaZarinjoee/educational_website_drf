# Generated by Django 5.0.4 on 2024-04-27 08:53

import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalgroup',
            name='image_educational_groups',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='iamge_teacher',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to),
        ),
    ]
