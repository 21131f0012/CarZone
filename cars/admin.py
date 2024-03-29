from django.contrib import admin
from .models import *
from django.utils.html import  format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;"/>'.format(object.car_photo.url))
    thumbnail.short_description='Car photo'
    list_display=('id','thumbnail','car_title','city','color', 'model', 'fuel_type', 'year','is_featured')
    list_display_links=('car_title','thumbnail')
    list_editable=('is_featured',)
    search_fields=('car_title','model','fuel_type')
    list_filter=('city','fuel_type','model')
admin.site.register(Car,CarAdmin)
