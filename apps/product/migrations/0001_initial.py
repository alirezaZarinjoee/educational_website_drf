# Generated by Django 5.0.4 on 2024-04-27 07:58

import django.db.models.deletion
import django.utils.timezone
import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250, verbose_name='full name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='date of added teacher')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='date of update teacher info')),
                ('is_active', models.BooleanField(blank=True, default=False, verbose_name='active/de_active')),
                ('image', models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='image of teacher')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', models.SlugField(max_length=260, null=True, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teachers',
            },
        ),
        migrations.CreateModel(
            name='EducationalGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100, verbose_name='group_name')),
                ('image', models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='image of EducationalGroup')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='date of added EducationalGroup')),
                ('is_active', models.BooleanField(blank=True, default=False, verbose_name='active/de_active')),
                ('slug', models.SlugField(max_length=260, null=True, unique=True, verbose_name='slug')),
                ('group_parent_educational', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='product.educationalgroup', verbose_name='group_parent_educational')),
            ],
            options={
                'verbose_name': 'educational group',
                'verbose_name_plural': 'educational groups',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200, verbose_name='Course name')),
                ('brief_description', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='image of EducationalGroup')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='date of added education')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='date of update education info')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='published_date')),
                ('is_active', models.BooleanField(blank=True, default=False, verbose_name='active/de_active')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('slug', models.SlugField(max_length=260, null=True, unique=True, verbose_name='slug')),
                ('group', models.ManyToManyField(related_name='educations_of_group', to='product.educationalgroup', verbose_name='group')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
            },
        ),
        migrations.CreateModel(
            name='EducationVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=100, verbose_name='video_name')),
                ('video', models.FileField(upload_to=utils.FileUpload.upload_to, verbose_name='video')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='slug')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='product.education', verbose_name='Education')),
            ],
            options={
                'verbose_name': 'video_education',
                'verbose_name_plural': 'videos_education',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=100, verbose_name='feature_name')),
                ('educational_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educational_group_features', to='product.educationalgroup', verbose_name='educational_group')),
            ],
            options={
                'verbose_name': 'feature',
                'verbose_name_plural': 'features',
            },
        ),
        migrations.CreateModel(
            name='EducationFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='value')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.education', verbose_name='education')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.feature', verbose_name='feature')),
            ],
            options={
                'verbose_name': 'education_feature',
                'verbose_name_plural': 'education_features',
            },
        ),
        migrations.AddField(
            model_name='education',
            name='feature',
            field=models.ManyToManyField(through='product.EducationFeature', to='product.feature', verbose_name='feature'),
        ),
        migrations.AddField(
            model_name='education',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations_of_teacher', to='product.teacher', verbose_name='teacher'),
        ),
    ]