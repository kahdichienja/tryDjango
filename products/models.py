from django.db import models

# Create your models here.


class Product(models.Model):
    title       = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=5, decimal_places=2)
    summary     = models.TextField(default = 'this is cool')
    featured    = models.NullBooleanField()