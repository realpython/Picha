# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name=b'Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name=b'Updated on')),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
                ('link', models.URLField(help_text=b'The URL to the image page', max_length=255, verbose_name=b'Photo Link')),
                ('image_url', models.URLField(help_text=b'The URL to the image file itself', max_length=255, verbose_name=b'Image URL')),
                ('description', models.TextField(verbose_name=b'Description')),
            ],
            options={
                'ordering': ['-created_on', 'title'],
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
    ]
