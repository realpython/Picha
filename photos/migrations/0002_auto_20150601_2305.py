# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created_on',
            field=models.DateTimeField(verbose_name='Created on', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_url',
            field=models.URLField(help_text='The URL to the image file itself', verbose_name='Image URL', max_length=255),
        ),
        migrations.AlterField(
            model_name='photo',
            name='link',
            field=models.URLField(help_text='The URL to the image page', verbose_name='Photo Link', max_length=255),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(verbose_name='Title', max_length=255),
        ),
        migrations.AlterField(
            model_name='photo',
            name='updated_on',
            field=models.DateTimeField(verbose_name='Updated on', auto_now=True),
        ),
    ]
