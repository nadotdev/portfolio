from django.contrib import admin
from portfolio.models import WorkingTimeline


class WorkingTimelineAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'started_date',
        'ended_date',
        'content'
    )
