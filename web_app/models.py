from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=30)
    product_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name_plural = 'Products'
