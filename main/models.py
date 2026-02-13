from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    def __str__(self): return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True)
    content = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True) 
    status = models.CharField(max_length=20, default='published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)