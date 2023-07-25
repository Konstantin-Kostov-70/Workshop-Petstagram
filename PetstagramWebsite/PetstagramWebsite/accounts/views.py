from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from PetstagramWebsite.accounts.forms import PetstagramUserCreateForm, UserLoginForm, UserEditForm
from PetstagramWebsite.accounts.models import PetstagramUser


class UserRegisterView(views.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home')


class UserLogoutView(auth_views.LogoutView):
    template_name = 'base.html'
    next_page = reverse_lazy('login')


class ProfileDetailsView(views.DetailView):
    model = PetstagramUser
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_like_count = sum(photo.like_set.count() for photo in self.object.photo_set.all())

        context['is_owner'] = self.request.user == self.object
        context['total_like_count'] = total_like_count

        return context


class ProfileEditView(views.UpdateView):
    model = PetstagramUser
    form_class = UserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class ProfileDeleteView(views.DeleteView):
    model = PetstagramUser
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home')





