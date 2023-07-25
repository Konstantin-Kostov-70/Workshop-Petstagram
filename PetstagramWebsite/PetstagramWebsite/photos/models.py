from django.db import models

from PetstagramWebsite.accounts.models import PetstagramUser
from PetstagramWebsite.pets.models import Pet
from PetstagramWebsite.photos.validators import validate_file_size
from django.core.validators import MinLengthValidator


class Photo(models.Model):
    image = models.ImageField(
        upload_to='pet_photos',
        validators=(validate_file_size,),
    )
    description = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        validators=(MinLengthValidator(10),),
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
    date_of_publication = models.DateField(
        auto_now=True
    )
    user = models.ForeignKey(
        to=PetstagramUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        pets = self.tagged_pets.all()
        names_list = [str(name) for name in pets]
        return f'{", ".join(names_list)}, ... are in this photo'
