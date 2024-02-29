from django.contrib import admin
from portfolio.models import WorkingTimeline, Education, Technology, About, Skill


admin.site.site_header="Cloudna Administration"

class WorkingTimelineAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'started_date',
        'ended_date',
        'content'
    )


admin.site.register(WorkingTimeline, WorkingTimelineAdmin)
admin.site.register(Education)
admin.site.register(Technology)
admin.site.register(About)
admin.site.register(Skill)