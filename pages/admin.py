from django.contrib import admin
from  .models import *
from django.utils.html import  format_html


# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def Photo(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;"/>'.format(object.photo.url))
    list_display = ('id','Photo','first_name','designation','created_date')
    list_display_links=('id','Photo')
    search_fields=('first_name','last_name','designation')
admin.site.register(Team,TeamAdmin)