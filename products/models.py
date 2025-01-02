from django.db import models
from django.utils import timezone
import uuid

class Basemodels(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(Basemodels):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=255, default="Uncategorized")
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name