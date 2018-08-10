from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)