from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_title = '后台管理系统'
admin.site.site_header = 'Commusic后台管理系统'

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']
    ordering = ['id']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id','name','author','release','text','file']
    search_fields = ['name','author']
    list_filter = ['author']
    ordering = ['id']

@admin.register(Dynamic)
class DynamicAdmin(admin.ModelAdmin):
    list_display = ['id', 'song', 'plays', 'search', 'download']
    search_fields = ['song']
    list_filter = ['plays', 'search', 'download']
    ordering = ['id']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user', 'song', 'date']
    search_fields = ['user','song','date']
    list_filter = ['song', 'date']
    ordering = ['id']