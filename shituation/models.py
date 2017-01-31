from django.db import models
from  django.utils import timezone


class Demo(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    cover = models.ImageField()

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    lyrics = models.TextField()
    youtube = models.URLField()
    demo = models.ForeignKey('Demo', null=True, related_name='songs')

    def __str__(self):
        return self.title

class Live(models.Model):
    live_date = models.DateField()
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=50, null=True)
    poster = models.ImageField()

    def __str__(self):
        return self.location

class Photos(models.Model):
    live = models.ForeignKey('Live', blank=True, null=True, related_name='photo')
    photo = models.ImageField()

    def __str__(self):
        return str(self.photo)

class LiveVideo(models.Model):
    live = models.ForeignKey('Live', blank=True, null=True, related_name='liveVideo')
    video = models.URLField()

    def __str__(self):
        return self.video

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    demo = models.ForeignKey('Demo', blank=True, null=True, related_name='post_demo')
    live = models.ForeignKey('Live', blank=True, null=True, related_name='post_live')
    photo = models.ForeignKey('Photos', blank=True, null=True)
    video = models.ForeignKey('LiveVideo', blank=True, null=True)
    song = models.ForeignKey('Song', blank=True, null=True)
    band = models.ForeignKey('Bands', blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self) -> object:
         return self.title

class Bands(models.Model):
    name = models.CharField(max_length=50)
    live = models.ForeignKey('Live', null=True, related_name='band')

    def __str__(self):
        return self.name



