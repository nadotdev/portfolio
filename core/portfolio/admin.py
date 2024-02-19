from django.contrib import admin

from portfolio.models import WorkingTimeline
# Register your models here.
class WorkingTimelineAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'started_date',
        'ended_date',
        'content'
    )
