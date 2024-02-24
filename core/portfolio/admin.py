from django.contrib import admin
from portfolio.models import WorkingTimeline


admin.site.site_header="Cloudna Administration"

class WorkingTimelineAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'started_date',
        'ended_date',
        'content'
    )


admin.site.register(WorkingTimeline, WorkingTimelineAdmin)
