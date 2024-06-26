# Generated by Django 5.0.4 on 2024-04-27 22:52

import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_alter_education_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='image',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='image of EducationalGroup'),
        ),
        migrations.AlterField(
            model_name='education',
            name='slug',
            field=models.SlugField(blank=True, default='<django.db.models.fields.CharField>', unique=True),
        ),
        migrations.AlterField(
            model_name='educationalgroup',
            name='image_educational_groups',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to),
        ),
        migrations.AlterField(
            model_name='educationvideos',
            name='video',
            field=models.FileField(upload_to=utils.FileUpload.upload_to, verbose_name='video'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='iamge_teacher',
            field=models.ImageField(blank=True, default='images/teachers/nophoto.jpg', upload_to=utils.FileUpload.upload_to),
        ),
    ]
