from django.db import models
from utils import FileUpload
from django.utils import timezone
from django.utils.text import slugify



class Writer(models.Model):
    name=models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name} {self.family}'


class Blog(models.Model):
    title=models.CharField(max_length=250)
    file_upload=FileUpload('images','blog')
    image=models.ImageField(upload_to=file_upload.upload_to,null=True,blank=True)
    text=models.TextField()
    is_active=models.BooleanField(default=False)
    register_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(default=timezone.now)
    writer=models.ForeignKey(Writer, on_delete=models.CASCADE,related_name='blogs')
    slug=models.SlugField(unique=True,blank=True)
    
    def save(self, *args, **kwargs): #function for save slug from fields
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='blog'
        verbose_name_plural='blogs'
        