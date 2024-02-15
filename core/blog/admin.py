from django.contrib import admin

from blog.models import Blog

# Register your models here.

admin.site.site_header = 'admin@cloudna.xyz'

admin.site.register(Blog)