# Generated by Django 5.0.4 on 2024-04-27 08:55

import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_educationalgroup_image_educational_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='educationalgroup',
            name='image_educational_groups',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='iamge_teacher',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to),
        ),
    ]
