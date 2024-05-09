from django.db import models
from utils import FileUpload
from django.utils import timezone
from django.utils.text import slugify


#---------------------------------------------------------------------------------------
class Teacher(models.Model):
    name=models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    email=models.EmailField(max_length=254,unique=True)
    file_uplaod=FileUpload('images','teachers')
    iamge_teacher=models.ImageField(upload_to=file_uplaod.upload_to,default='images/teachers/nophoto.jpg',blank=True)
    descriptions=models.TextField(null=True,blank=True)
    join_time=models.DateTimeField(default=timezone.now,blank=True)
    is_active=models.BooleanField(default=True,blank=True)
    slug=models.SlugField(unique=True,blank=True)#Note: Never use max_length feature for slug
    
    def __str__(self):
        return f'{self.name}-{self.family}'
    
    def save(self, *args, **kwargs): #function for save slug from fields
        if not self.slug:
            self.slug = slugify(self.name + "-" + self.family)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name='teacher'
        verbose_name_plural='teachers'
        
#---------------------------------------------------------------------------------------

class EducationalGroup(models.Model):
    group_title=models.CharField(max_length=100)
    file_upload=FileUpload('images','EducationalGroups')
    image_educational_groups=models.ImageField(upload_to=file_upload.upload_to)
    description=models.TextField(null=True,blank=True)
    is_active=models.BooleanField(default=True,blank=True)
    group_parent=models.ForeignKey('EducationalGroup', on_delete=models.CASCADE,related_name='groups',null=True,blank=True)
    slug=models.SlugField(unique=True,max_length=200,null=True,blank=True)#Note: Never use max_length feature for slug
    register_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.group_title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.group_title
    
    class Meta:
        verbose_name = 'educational_group'
        verbose_name_plural = 'educational_groups'
        
# #---------------------------------------------------------------------------------------
# # model of feature 
class Feature(models.Model):
    feature_name=models.CharField(verbose_name='feature_name', max_length=100)
    educational_group=models.ForeignKey(EducationalGroup, verbose_name='educational_group', on_delete=models.CASCADE,related_name='educational_group_features')
    
    def __str__(self):
        return self.feature_name
    
    class Meta:
        verbose_name='feature'
        verbose_name_plural='features'
#---------------------------------------------------------------------------------------
# # model of Education
class Education(models.Model):
    course_name=models.CharField(verbose_name='Course name', max_length=200)
    brief_description=models.TextField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    file_upload=FileUpload('images','Education')
    image=models.ImageField(verbose_name='image of EducationalGroup', upload_to=file_upload.upload_to)
    register_date=models.DateTimeField(verbose_name='date of added education', auto_now_add=True)
    update_date=models.DateTimeField(verbose_name='date of update education info', auto_now=True)
    published_date=models.DateTimeField(verbose_name='published_date',default=timezone.now)
    is_active=models.BooleanField(verbose_name='active/de_active',default=False,blank=True)
    price=models.PositiveIntegerField(verbose_name='price')
    slug=models.SlugField(unique=True,blank=True)#Note: Never use max_length feature for slug
    teacher=models.ForeignKey(Teacher, verbose_name='teacher', on_delete=models.CASCADE,related_name='educations_of_teacher')
    group=models.ManyToManyField(EducationalGroup, verbose_name='group',related_name='educations_of_group')
    feature=models.ManyToManyField(Feature, verbose_name='feature',through='EducationFeature')  #By adding the through feature, we can prevent the creation of the third table by orm and write a third table for it ourselves, which we can customize.
    
    def price_of_education(self):
        tax=0.05
        return self.price+(self.price*tax)
       
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.course_name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.course_name
    
    class Meta:
        verbose_name='Education'
        verbose_name_plural='Educations'
# #---------------------------------------------------------------------------------------
class FeatureValue(models.Model):
    value_title=models.CharField(verbose_name='value_title',max_length=100)
    feature=models.ForeignKey(Feature, verbose_name='feature',null=True,blank=True,on_delete=models.CASCADE,related_name='feature_values')

    def __str__(self):
        return f'{self.id} - {self.value_title}'
    
    class Meta:
        verbose_name='feature_value'
        verbose_name_plural='feature_values'

# #---------------------------------------------------------------------------------------
# # model of EducationFeature
class EducationFeature(models.Model):
    education=models.ForeignKey(Education, verbose_name='education', on_delete=models.CASCADE)
    feature=models.ForeignKey(Feature, verbose_name='feature', on_delete=models.CASCADE)
    value=models.CharField(verbose_name='value', max_length=100)
    filter_value=models.ForeignKey(FeatureValue, verbose_name='filter_value',null=True,blank=True, on_delete=models.CASCADE,related_name='feature_values')
    
    def __str__(self):
        return f'{self.education} - {self.feature} : {self.value}'
    
    class Meta:
        verbose_name='education_feature'
        verbose_name_plural='education_features'
        
# #---------------------------------------------------------------------------------------
class EducationVideos(models.Model):
    video_name=models.CharField(verbose_name='video_name', max_length=100)
    education=models.ForeignKey(Education, verbose_name='Education', on_delete=models.CASCADE,related_name='videos')
    file_upload=FileUpload('videos','videos_education')
    video=models.FileField(verbose_name='video',upload_to=file_upload.upload_to)
    slug=models.SlugField(unique=True,blank=True)#Note: Never use max_length feature for slug
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.video_name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name='video_education'
        verbose_name_plural='videos_education'
    
#---------------------------------------------------------------------------------------
