from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite


class Demo_Admin(admin.ModelAdmin):
    list_display = ('name', 'date', 'cover')
    list_filter = ('name', 'date')
    search_fields = ('name', 'date')

class Song_Admin(admin.ModelAdmin):
    list_display = ('title', 'youtube', 'demo')
    list_filter = ('title', 'demo')
    search_fields = ('title', 'demo__name')

class Live_Admin(admin.ModelAdmin):
    list_display = ('location', 'city', 'live_date', 'poster')
    list_editable = ('poster', 'poster')
    list_filter = ('location', 'city', 'live_date')
    search_fields = ('location', 'city', 'live_date')

class Photos_Admin(admin.ModelAdmin):
    list_display = ('live', 'photo')
    list_editable = ('photo', 'photo')
    list_filter = ('live', 'live__city', 'live__live_date')
    search_fields = ('live__location', 'live__city', 'live__live_date')

class LiveVideo_Admin(admin.ModelAdmin):
    list_display = ('live', 'video')
    list_editable = ('video', 'video')
    list_filter = ('live', 'live__city', 'live__live_date')
    search_fields = ('live__location', 'live__city', 'live__live_date')

class Post_Admin(admin.ModelAdmin):
    list_display = ('author', 'title','published_date','song','live','photo','video')
    list_display_links = ('title','title')
    list_filter = ('author', 'published_date','live','live__city')
    search_fields = ('title', 'published_date', 'live__city', 'live__location','live__live_date', 'photo__live__live_date', 'video__live__live_date')


class My_Admin(AdminSite):
    site_header = 'Shituation Site Administration'
    site_title = 'Shituation'



admin.site= My_Admin(name='my_admin')

admin.site.register(Demo, Demo_Admin)
admin.site.register(Song, Song_Admin)
admin.site.register(Live, Live_Admin)
admin.site.register(LiveVideo, LiveVideo_Admin)
admin.site.register(Photos, Photos_Admin)
admin.site.register(Post, Post_Admin)
admin.site.register(Bands)


