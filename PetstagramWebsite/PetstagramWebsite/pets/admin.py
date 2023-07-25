from django.contrib import admin

from PetstagramWebsite.pets.models import Pet


@admin.register(Pet)
class PetsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']


