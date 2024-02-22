# Generated by Django 5.0.2 on 2024-02-21 15:47

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_about_education_technology'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='describe',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Describe'),
        ),
    ]
