from django.db import models

# Create your models here.

import uuid

class Basemodels(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_created=True)

    class Meta:
        abstract = True # This will not create a table for this model

class Product(Basemodels):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class ProductImage(Basemodels):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return self.product.name
    
class ProductMetaInformation(Basemodels):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="meta_info")
    quantity = models.IntegerField(null=True, blank=True)
    is_restrict = models.BooleanField(default=False)
    restrict_quantity = models.IntegerField(null=True, blank=True)
    key = models.CharField(max_length=255)
    value = models.TextField()

    def __str__(self):
        return self.product.name