from django.urls import path
from . import views


urlpatterns = [
    path("register", views.register, name='register'),
    # path('login/', views.custom_login_view, name='custom_login'),
]
