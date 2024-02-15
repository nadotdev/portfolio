
from django.contrib import admin
from django.urls import include, path
from core import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("portfolio.urls")),
    path("blogs", include("blog.urls")),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
