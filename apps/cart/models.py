from django.db import models
from apps.account.models import CustomUser
from apps.product.models import Education
from apps.account.models import Customer
from django.utils import timezone
import uuid

class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='product_of_user')
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    register_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.email}-{self.education.course_name}"


class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='orders')
    register_date=models.DateField(default=timezone.now)
    update_date=models.DateField(auto_now=True)
    is_finaly=models.BooleanField(default=False)
    order_code=models.UUIDField(unique=True,default=uuid.uuid4,editable=False)
    discount=models.IntegerField(blank=True,null=True,default=0)#OFF on factor
    
    def __str__(self):
        return f'{self.customer} - {self.id} - {self.is_finaly}'
    
    class Meta:
        verbose_name='order'
        verbose_name_plural='orders'
        
        
class OrderDetail(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE,related_name='order_details_1')
    education=models.ForeignKey(Education, on_delete=models.CASCADE,related_name='order_details_2')
    price=models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.order} - {self.education} - {self.price}'
    
    class Meta:
        verbose_name='order detail'
        verbose_name_plural='order details'
        
        