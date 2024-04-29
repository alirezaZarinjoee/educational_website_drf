from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=('name','family','email','slug','is_active')
    search_fields=('family','name')
    ordering=('join_time','family','is_active')
    list_filter=('is_active',)
    list_editable=['is_active']
    
