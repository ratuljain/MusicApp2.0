from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='post_list'),
    url(r'^track/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^track/new/$', views.post_new, name='post_new'),
    url(r'^track/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^genre/$', views.genre, name='genre_list'),
    url(r'^genre/(?P<pk>\d+)/$', views.genre_songs, name='genre_songs'),
    url(r'^genre/new/$', views.genre_new, name='genre_new'),
    url(r'^genre/(?P<pk>\d+)/edit/$', views.genre_edit, name='genre_edit'),
]
