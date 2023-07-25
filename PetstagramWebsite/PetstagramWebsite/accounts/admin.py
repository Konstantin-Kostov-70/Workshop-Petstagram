from django.contrib import admin
from PetstagramWebsite.accounts.models import PetstagramUser


@admin.register(PetstagramUser)
class PetstagramUserAdmin(admin.ModelAdmin):
    pass
