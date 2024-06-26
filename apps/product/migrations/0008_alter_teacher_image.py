# Generated by Django 5.0.4 on 2024-04-27 08:16

import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_teacher_full_name_alter_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='image of teacher'),
        ),
    ]
