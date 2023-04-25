from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import VideoForm
from modelCore.models import *
from modelCore.tasks.tasks import *
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from web.camera import  VideoCamera


def gen(camera):
        while True:
            # try:
                frame = camera.get_frame(camera)
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
def video_feed(request):
    video_id =  request.GET.get('video_id')
    video = Video.objects.get(id=video_id)
    dic = video.data
    video_path = video.video_file.path
    response = StreamingHttpResponse(gen(VideoCamera(dic=dic,video_path=video_path,video_id=video_id),),
					content_type='multipart/x-mixed-replace; boundary=frame')


    return response
    
def home(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'home.html', context)

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            video.save()
            video_id = video.id
            store_video_data(video_id, 0)
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def select_video(request):
    video = None
    if request.method == 'POST':
        video_id = request.POST.get('video_selection')
        video = Video.objects.get(id=video_id)
    videos = Video.objects.all()
    return render(request, 'select_video.html', {'videos': videos, 'selected_video': video})

def dance_detect(request):
    video_id =  request.GET.get('video_id')
    video = Video.objects.get(id=video_id)
    request.session['i'] = '0'
    request.session['list'] = '[0]'
    request.session['DIC'] = '{"LEFTELBOW":[],"RIGHTELBOW":[],"LEFTSHOULDER":[],"RIGHTSHOULDER":[],"LEFTHIP":[],"RIGHTHIP":[],"LEFTKNEE":[],"RIGHTKNEE":[]}'
    return render(request, 'dance_detect.html',{'video':video,'video_id':video_id} )

def game_score(request):
    video_id =  request.GET.get('video_id')
    video = Video.objects.get(id=video_id)
    user = User.objects.get(id=1)
    gameScore = GameScore.objects.filter(user=user,video=video).order_by('-date').first()
    return render(request, 'game_score.html',{'video':video,'user':user,'gameScore':gameScore})


