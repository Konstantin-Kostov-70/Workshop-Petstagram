from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator

from PetstagramWebsite.accounts.validators import only_letters_validator


class PetstagramUser(AbstractUser):
    email = models.EmailField(
        unique=True
    )

    first_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_letters_validator,
        )
    )

    last_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_letters_validator,
        )
    )

    profile_picture = models.URLField()

    gender = models.CharField(
        max_length=20,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Do not show', 'Do not show'),
        ),
    )

