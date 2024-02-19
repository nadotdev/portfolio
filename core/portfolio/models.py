from django.db import models
from datetime import date
from django_ckeditor_5.fields import CKEditor5Field
class WorkingTimeline(models.Model):
    """For my portfoili working background as timelines."""
    title = models.CharField(max_length=255, blank=False, null=False, default=None)
    started_date = models.DateField(default=date.today, blank=False, null=False)
    ended_date = models.DateField(default=date.today, blank=False, null=False)
    content = CKEditor5Field('Content', config_name='extends')