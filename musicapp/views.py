from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect
from .forms import AddTrackForm, AddGenreForm
from django.http import HttpResponse
from .models import Track, Genre
from . import getAlbumArt
from django.core.urlresolvers import reverse
from haystack.management.commands import update_index
# Create your views here.
def home(request):
    tracks = Track.objects.all().order_by('created_date')
    return render(request, 'musicapp/post_list.html', {'tracks': tracks})

def post_detail(request, pk):
    track = get_object_or_404(Track, pk=pk)
    # print post
    return render(request, 'musicapp/post_detail.html', {'track': track})
# def post_new(request):
#     form = AddTrackForm()
#     return render(request, 'musicapp/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = AddTrackForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            artist = request.POST.get("artist", "")
            album = request.POST.get("album", "")
            # print artist, album
            urlArt = getAlbumArt.getAlbumArtURL(album, artist)
            print urlArt
            if urlArt:
                post.cover_image_url = urlArt
            if post.album == '*':
                post.album = 'Unknown'
            post.save()
            tracks = Track.objects.all().order_by('created_date')
            return HttpResponseRedirect(reverse('post_list'))
            # return render(request, 'musicapp/post_list.html', {'tracks': tracks})
    else:
        form = AddTrackForm()
    return render(request, 'musicapp/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Track, pk=pk)
    if request.method == "POST":
        form = AddTrackForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            artist = request.POST.get("artist", "")
            album = request.POST.get("album", "")
            # print artist, album
            urlArt = getAlbumArt.getAlbumArtURL(album, artist)
            print urlArt
            if urlArt:
                post.cover_image_url = urlArt
            if post.album == '*':
                post.album = 'Unknown'
            post.save()
            tracks = Track.objects.all().order_by('created_date')
            return redirect('post_detail', pk=post.pk)
    else:
        form = AddTrackForm(instance=post)
    return render(request, 'musicapp/post_edit.html', {'form': form})

def genre(request):
    tracks = Track.objects.all().order_by('created_date')
    genres = Genre.objects.all()
    return render(request, 'musicapp/genre.html', {'genres': genres, 'tracks': tracks})

def genre_songs(request, pk):
    genres = Genre.objects.all()
    genre_obj = get_object_or_404(Genre, pk=pk)
    tracks = genre_obj.track_set.all()
    # print post
    return render(request, 'musicapp/genre_songs.html', {'genres': genres, 'genre' : genre_obj, 'tracks': tracks})

def genre_new(request):
    if request.method == "POST":
        form = AddGenreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            redirect_flag = request.POST.get("flag", "")  # redirect to different places depending upon where it was clicked
            post.save()
            genres = Genre.objects.all()
            print redirect_flag
            if redirect_flag == '0':
                return HttpResponseRedirect(reverse('post_new'))
            elif redirect_flag == '1':
                return HttpResponseRedirect(reverse('genre_list'))
            else:
                return HttpResponseRedirect('/')
            # return render_to_response('musicapp/genre.html', {'form': AddTrackForm()})
    else:
        form = AddGenreForm()
    return render(request, 'musicapp/genre_edit.html', {'form': form})

def genre_edit(request, pk):
    post = get_object_or_404(Genre, pk=pk)
    if request.method == "POST":
        form = AddGenreForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            
            return redirect('genre_songs', pk=post.pk)
            # return HttpResponseRedirect(reverse('genre_list'))
    else:
        form = AddGenreForm(instance=post)
    return render(request, 'musicapp/genre_edit.html', {'form': form})
