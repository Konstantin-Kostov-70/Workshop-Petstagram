from django.urls import path

from PetstagramWebsite.photos.views import photos_add, photos_details, photos_edit, photos_delete

urlpatterns = [
    path('add/', photos_add, name='photo_add'),
    path('<int:pk>/', photos_details, name='photo_details'),
    path('edit/<int:pk>', photos_edit, name='photo_edit'),
    path('delete/<int:pk>', photos_delete, name='photo_delete')
]