# Generated by Django 5.0.4 on 2024-04-27 08:10

import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_educationfeature_education_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='educational_group',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='image of teacher'),
        ),
        migrations.DeleteModel(
            name='EducationalGroup',
        ),
        migrations.DeleteModel(
            name='Feature',
        ),
    ]
