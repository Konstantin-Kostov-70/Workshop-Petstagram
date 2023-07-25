from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from PetstagramWebsite.common.forms import CommentForm
from PetstagramWebsite.photos.forms import PhotoCreateForm, PhotoEditForm
from PetstagramWebsite.photos.models import Photo


@login_required
def photos_add(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'photos/photo-add-page.html', context)


def photos_details(request, pk):
    photo_is_liked_by_user = None
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()

    if request.user.is_authenticated:
        photo_is_liked_by_user = likes.filter(user=request.user)

    comments = photo.comment_set.all()
    comment_form = CommentForm()
    is_owner = photo.user == request.user

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
        'is_owner': is_owner,
        'photo_is_liked_by_user':  photo_is_liked_by_user
    }
    return render(request, 'photos/photo-details-page.html', context)


def photos_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo, initial=photo.__dict__)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo_details', pk)
    context = {
        'form': form,
        'photo': photo
    }
    return render(request, 'photos/photo-edit-page.html', context)


def photos_delete(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home')
