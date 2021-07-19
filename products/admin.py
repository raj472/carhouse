from django.contrib import admin
from .models import Team
from django.contrib import admin
from .models import Team
from django.utils.html import format_html #this makes html work in python files, thus we can work using html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):  # this function makes  thumbnail(putting photo)
        return format_html('<img src = "{}" width ="40" style ="border_radius:100px"/>'.format(object.photo.url))

    thumbnail.short_description = 'photo'



# here the list variable are inbuilt
    list_display = ("id","thumbnail", "first_name", "designation","create_date",) #order is customisable
    list_display_links = ("id", "first_name","thumbnail",)  #making clickable
    search_fields = ("first_name","last_name", "designation",) #making search function
    list_filter = ("designation",)  #filtering



admin.site.register(Team, TeamAdmin)





