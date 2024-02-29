from django.db import models
from datetime import date
from django_ckeditor_5.fields import CKEditor5Field


class Education(models.Model):
    """
        For my portfolio education background as timelines.
    """
    # label = models.CharField(max_length=255, blank=False, null=False, default=None)
    title = models.CharField(max_length=255, blank=False, null=False, default=None)
    started_date = models.DateField(default=date.today, blank=False, null=False)
    ended_date = models.DateField(default=date.today, blank=False, null=False)
    content = CKEditor5Field('Content', config_name='extends')


class WorkingTimeline(models.Model):
    """
        For my portfolio working background as timelines.
    """
    # label = models.CharField(max_length=255, blank=False, null=False, default=None)
    title = models.CharField(max_length=255, blank=False, null=False, default=None)
    started_date = models.DateField(default=date.today, blank=False, null=False)
    ended_date = models.DateField(default=date.today, blank=False, null=False)
    content = CKEditor5Field('Content', config_name='extends')


class About(models.Model):
    """
    Describe about me
    """
    describe = CKEditor5Field('Describe', config_name='extends')
    created_at = models.DateField(auto_now=True)


class Technology(models.Model):
    """
    Describe what technologies that I have used as a developer.
    """
    title = models.CharField(max_length=255, blank=False, null=False, default=None)
    sub_title = models.CharField(max_length=255, blank=False, null=False, default=None)


class Skill(models.Model):
    """
        Skill timelines
    """
    title = models.CharField(max_length=255, blank=False, null=False, default=None)
