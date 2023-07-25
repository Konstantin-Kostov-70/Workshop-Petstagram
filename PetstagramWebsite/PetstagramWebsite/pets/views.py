from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from PetstagramWebsite.common.core import get_all_liked_photos_by_request_user
from PetstagramWebsite.common.forms import CommentForm
from PetstagramWebsite.pets.forms import PetForm, PetDeleteForm
from PetstagramWebsite.pets.models import Pet


@login_required
def pet_add(request):
    if request.method == 'GET':
        form = PetForm()
    else:
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()

            return redirect('profile-details', pk=request.user.pk)

    context = {
        'form': form
    }
    return render(request, 'pets/pet-add-page.html', context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    is_owner = pet.user == request.user
    username = username
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'username': username,
        'all_photos': all_photos,
        'comment_form': comment_form,
        'is_owner': is_owner,
        'all_liked_photos_by_request_user':  get_all_liked_photos_by_request_user(request),
    }
    return render(request, 'pets/pet-details-page.html', context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_details', username, pet_slug)
    context = {
        'form': form,
        'pet': pet
    }
    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('home')
    form = PetDeleteForm(initial=pet.__dict__)
    context = {
        'form': form,
        'pet': pet
    }
    return render(request, 'pets/pet-delete-page.html', context)
