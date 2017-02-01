from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^demos/$', views.demos_albums, name='demos_albums'),
    url(r'^demos/demo/(?P<pk>[0-9]+)/$', views.demo_details, name='demo_details'),
    url(r'^demos/demo/lyrics/(?P<pk>[0-9]+)/$', views.lyrics, name='lyrics'),
    url(r'^live/$', views.live, name='live'),
    url(r'^live/details/(?P<pk>[0-9]+)/$', views.live_details, name='live_details'),
    url(r'^live/details/videos/(?P<pk>[0-9]+)/$', views.live_videos, name='live_videos'),
    url(r'^live/details/photos/(?P<pk>[0-9]+)/$', views.live_photos, name='live_photos'),
    url(r'^about/$', views.about, name='about')

]
