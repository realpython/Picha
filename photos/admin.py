from django.contrib import admin

from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
