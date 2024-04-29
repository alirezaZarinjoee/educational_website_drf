# Generated by Django 5.0.4 on 2024-04-27 08:09

import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationfeature',
            name='education',
        ),
        migrations.RemoveField(
            model_name='educationfeature',
            name='feature',
        ),
        migrations.AlterField(
            model_name='educationalgroup',
            name='image',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='image of EducationalGroup'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='image of teacher'),
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='EducationFeature',
        ),
    ]
