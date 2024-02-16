from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True, null=False, blank=False)
    thumbnail = models.ImageField(upload_to='blog_thumbnail')
    slug = models.SlugField(default="", null=False)
    description = CKEditor5Field('Text', config_name='extends')
    posted_date = models.DateField(auto_now=True)
    