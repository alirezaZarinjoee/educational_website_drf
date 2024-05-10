from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from apps.product.models import Education


class Coupon(models.Model):
    coupon_code=models.CharField(unique=True, max_length=10)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    discount_percent=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    is_active=models.BooleanField(default=False)
    def __str__(self):
        return self.coupon_code
    class Meta:
        verbose_name='discount code'
        verbose_name_plural='discount codes'
        
        
#--------------------------------------------------------------------------------------------

class DiscountBasket(models.Model):
    discount_title=models.CharField(unique=True, max_length=10)
    start_date1=models.DateTimeField()
    end_date1=models.DateTimeField()
    discount_percent=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    is_active=models.BooleanField(default=False)
    def __str__(self):
        return self.discount_title
    class Meta:
        verbose_name='discount basket'
        verbose_name_plural='discount baskets'
        
#--------------------------------------------------------------------------------------------

class DiscountBasketDetails(models.Model):
    discount_basket=models.ForeignKey(DiscountBasket, on_delete=models.CASCADE,related_name='discount_basket_details1')
    product=models.ForeignKey(Education,on_delete=models.CASCADE,null=True,blank=True,related_name='discount_basket_details2')