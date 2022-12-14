from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=50, null=True, blank=True)
    content=models.CharField(max_length=50, null=True, blank=True)
    img=models.ImageField(upload_to="blog_img", null=True, blank=True)
    sitetitle=models.CharField(max_length=50, null=True, blank=True)
    site=models.URLField(max_length=200, null=True, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.title