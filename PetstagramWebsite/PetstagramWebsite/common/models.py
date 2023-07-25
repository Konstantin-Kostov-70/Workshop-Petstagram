from django.db import models

from PetstagramWebsite.accounts.models import PetstagramUser
from PetstagramWebsite.photos.models import Photo


class Comment(models.Model):
    text = models.TextField(
        max_length=300
    )
    date_time_of_publication = models.DateTimeField(
        auto_now_add=True
    )
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=PetstagramUser,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=PetstagramUser,
        on_delete=models.CASCADE
    )
