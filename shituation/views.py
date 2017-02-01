from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.db.models import Q

def song_list(request):
    songs = Song.objects.all()
    demo = Demo.objects.get(name='Hell')
    return render(request, 'shituation/song_list.html', {'songs': songs, 'demo':demo})

def home_page(request):
    search = request.GET.get('search','')
    date = request.GET.get('date','')
    photo =request.GET.get('photo','')
    if(date==''):
        if(search==''):
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        else:
            posts = Post.objects.filter((Q(title__contains=search) | Q(text__contains=search) | Q(author__username__contains=search)
                                        |Q(song__title__contains=search)|Q(song__demo__name__contains=search)
                                        |Q(photo__live__location__contains=search)|Q(photo__live__city__contains=search)
                                        |Q(video__live__location__contains=search)|Q(video__live__city__contains=search)
                                        |Q(live__city__contains=search)|Q(live__location__contains=search)
                                        & Q(published_date__lte=timezone.now()))).order_by('-published_date')
    else:
            posts = Post.objects.filter(published_date__lte=date).order_by('-published_date')
    return render(request, 'shituation/home_page.html', {'posts': posts})

def demos_albums(request):
    demos = Demo.objects.all()
    return  render(request, 'shituation/demos_albums.html', {'demos': demos})

def demo_details(request, pk):
    demo = get_object_or_404(Demo, pk=pk)
    songs = Song.objects.filter(demo__pk=pk)
    return render(request, 'shituation/demo_details.html',{'demo':demo, 'songs':songs})

def lyrics(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'shituation/lyrics.html',{'song':song})

def live(request):
    lives = Live.objects.all()
    return render(request, 'shituation/live.html', {'lives':lives})

def live_details(request, pk):
    live_= get_object_or_404(Live, pk=pk)
    return render(request, 'shituation/live_details.html', {'live_':live_})

def live_videos(request, pk):
    live_=get_object_or_404(Live, pk=pk)
    live_videos = LiveVideo.objects.filter(live__pk=pk)
    return render(request, 'shituation/live_videos.html',{'live_videos':live_videos, 'live_':live_})

def live_photos(request, pk):
    live_=get_object_or_404(Live, pk=pk)
    live_photos = Photos.objects.filter(live__pk=pk)
    return render(request, 'shituation/live_photos.html',{'live_photos':live_photos, 'live_':live_})

def about(request):
    return render(request, 'shituation/about.html')