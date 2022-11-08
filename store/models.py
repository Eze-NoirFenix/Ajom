from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)
    detail = models.CharField(max_length=50, null=True, blank=True)
    sitetitle=models.CharField(max_length=50, null=True, blank=True)
    site=models.URLField(max_length=200, null=True, blank=True)
    img = models.ImageField(upload_to='store', null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    stock = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return self.title