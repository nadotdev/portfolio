from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view, name='blogs-list'),
    path('detail/<int:pk>', views.blog_detail, name='blog-detail')
]
