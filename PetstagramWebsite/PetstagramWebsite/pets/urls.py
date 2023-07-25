from django.urls import path, include

from PetstagramWebsite.pets.views import pet_add, pet_details, pet_edit, pet_delete

urlpatterns = [
    path('add/', pet_add, name='pet_add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', pet_details, name='pet_details'),
        path('edit/', pet_edit, name='pet_edit'),
        path('delete/', pet_delete, name='pet_delete'),
    ]))
]