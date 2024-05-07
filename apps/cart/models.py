from django.db import models
from apps.account.models import CustomUser
from apps.product.models import Education

class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='product_of_user')
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    register_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.username}-{self.item.product_identifier}"

