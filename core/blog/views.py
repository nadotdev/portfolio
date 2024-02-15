from django.shortcuts import render
from .models import Blog

# Create your views here.

def blog_view(request):
    blogs = Blog.objects.all().order_by('posted_date')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blog.html', context)