# Generated by Django 5.0.2 on 2024-02-21 15:13

import datetime
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default=None, max_length=255)),
                ('describe', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=255)),
                ('started_date', models.DateField(default=datetime.date.today)),
                ('ended_date', models.DateField(default=datetime.date.today)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default=None, max_length=255)),
                ('title', models.CharField(default=None, max_length=255)),
                ('sub_title', models.CharField(default=None, max_length=255)),
            ],
        ),
    ]
