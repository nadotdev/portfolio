
from django.contrib import admin
from django.urls import include, path
from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("portfolio.urls")),
]