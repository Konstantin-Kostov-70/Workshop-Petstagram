from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from PetstagramWebsite.common.core import get_all_liked_photos_by_request_user
from PetstagramWebsite.common.forms import CommentForm, SearchForm
from PetstagramWebsite.common.models import Like
from PetstagramWebsite.photos.models import Photo


def index(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])
            search_form = SearchForm()

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
        'all_liked_photos_by_request_user': get_all_liked_photos_by_request_user(request),
    }
    return render(request, 'common/home-page.html', context)


@login_required
def like_functionality(request, photo_id):
    # photo = Photo.objects.get(id=photo_id)
    liked_photo = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()

    if liked_photo:
        liked_photo.delete()
    else:
        # like = Like(to_photo=photo)
        # like.save()
        Like.objects.create(to_photo_id=photo_id, user=request.user)
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required()
def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo_details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required()
def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)
        user = request.user
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = user
            comment.save()
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


