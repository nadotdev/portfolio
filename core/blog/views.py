from django.shortcuts import render
from .models import Blog

def blog_view(request):
    blogs = Blog.objects.all().order_by('-posted_date')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, pk):
    blog = Blog.objects.filter(pk=pk).get()
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context)