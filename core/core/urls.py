from django.urls import include, path
from blog.models import Blog
from core import settings
from django.conf.urls.static import static

from django.contrib.auth.models import User

from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin

from portfolio.models import WorkingTimeline, Education, About, Technology
from portfolio.admin import WorkingTimelineAdmin


class OTPAdmin(OTPAdminSite):
   pass


admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)
admin_site.register(Blog)
admin_site.register(WorkingTimeline, WorkingTimelineAdmin)
admin_site.register(Education)
admin_site.register(About)
admin_site.register(Technology)


admin_site.site_header = "admin@clounda.xyz"


urlpatterns = [
    path('admin/', admin_site.urls),
    path("", include("portfolio.urls")),
    path("blogs/", include("blog.urls")),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
