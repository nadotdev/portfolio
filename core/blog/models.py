from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True, null=False, blank=False)
    thumbnail = models.ImageField(upload_to='blog_thumbnail')
    slug = models.SlugField(default="", null=False)
    description = models.TextField(null=True, blank=True)
    posted_date = models.DateField(auto_now=True)
    