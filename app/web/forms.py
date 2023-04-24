from django import forms
from modelCore.models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['id','title', 'description', 'video_file']