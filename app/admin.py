from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_link = ('id', 'title')

admin.site.register(Photo, PhotoAdmin)
