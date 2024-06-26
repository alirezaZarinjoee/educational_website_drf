# Generated by Django 5.0.4 on 2024-04-27 08:10

import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_feature_educational_group_alter_teacher_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='full_name',
            field=models.CharField(max_length=250, verbose_name='full_name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='image of teacher'),
        ),
    ]
