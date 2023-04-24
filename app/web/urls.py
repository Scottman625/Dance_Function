from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('upload_video', views.upload_video, name = 'upload_video'), 
    path('select_video', views.select_video, name = 'select_video'),
    path('dance_detect', views.dance_detect, name = 'dance_detect'),
    path('game_score', views.game_score, name = 'game_score'),

    path('video_feed', views.video_feed, name='video_feed'),
]