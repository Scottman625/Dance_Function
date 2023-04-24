from django.contrib import admin

from .models import User, Video, GameScore

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'line_id')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_date')

@admin.register(GameScore)
class GameScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'video', 'score', 'date')
# Register your models here.
