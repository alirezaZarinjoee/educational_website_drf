from django.db import models
from apps.product.models import Education
from apps.account.models import CustomUser


class Comment(models.Model):
    education=models.ForeignKey(Education, on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='comments_of_user')
    text=models.TextField()
    is_active=models.BooleanField(default=True)
    register_date=models.DateTimeField(auto_now_add=True)
    parent=models.ForeignKey('Comment', on_delete=models.CASCADE,related_name='comments_child',null=True,blank=True)
    
    def __str__(self):
        return f'{self.education} - {self.user} - {self.text}'
    
    class Meta:
        verbose_name='comment'
        verbose_name_plural='comments'
        
 