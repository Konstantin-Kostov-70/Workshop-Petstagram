from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from PetstagramWebsite.accounts.models import PetstagramUser


class PetstagramUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = PetstagramUser
        fields = ['username', 'email']


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Password'
            }
        )
    )


class UserEditForm(forms.ModelForm):
    class Meta:
        model = PetstagramUser
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture', 'gender']
        exclude = ['password']
        labels = {
            'username': 'Username',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'email': 'Email:',
            'profile_picture': 'image:',
            'gender': 'Gender:'
        }
