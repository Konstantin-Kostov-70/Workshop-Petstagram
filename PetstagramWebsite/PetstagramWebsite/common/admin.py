from django.contrib import admin
from PetstagramWebsite.common.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'date_time_of_publication']


